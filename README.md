# Figpack Overview Presentation

[View the presentation](https://magland.github.io/figpack-overview-presentation/?slide=1)

## Development

Install dependencies:

```bash
pip install figpack numpy pandas matplotlib
figpack extensions install figpack_slides
npm install
```

First build the presentation:

```bash
python index.py
```

Then serve it locally:

```bash
npx serve build
```

Or in watch mode:

```bash
./dev.sh
```

Open your browser to:

```
http://localhost:3000/
```

If you want to be able to edit the presentation content from within the browser, you can run:

```bash
./dev.sh --edit
```

and then add the edit=1 parameter to the URL, e.g.:

```
http://localhost:3000/?edit=1
```
