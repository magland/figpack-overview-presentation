#!/bin/bash

# Array to store background process PIDs
PIDS=()

# Cleanup function to kill all background processes
cleanup() {
  echo "Cleaning up background processes..."
  for pid in "${PIDS[@]}"; do
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null
    fi
  done
  exit 0
}

# Set up trap to catch SIGINT (Ctrl+C), SIGTERM, and EXIT
trap cleanup SIGINT SIGTERM EXIT

# Start nodemon with inline configuration and serve in the background
# nodemon rebuilds the presentation when files change
# serve serves the built presentation on http://localhost:3000

npx nodemon \
  --watch . \
  --ext md,py \
  --ignore build/ \
  --ignore node_modules/ \
  --exec "python index.py" &
PIDS+=($!)

npx serve build -l 3000 &
PIDS+=($!)

# If we received the --edit flag anywhere in the options, also run figpack-slides-serve index.md
for arg in "$@"; do
  if [ "$arg" == "--edit" ]; then
    figpack-slides-serve index.md &
    PIDS+=($!)
  fi
done

# Wait for all background processes
wait
