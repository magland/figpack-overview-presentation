# Figpack Slides Demo Presentation

```yaml slide-metadata
slide-type: title
subtitle: How to create an interactive slide presentation using figpack_slides
author: Jeremy Magland, Center for Computational Mathematics, Flatiron Institute
```

---

# Outline

* What are Figpack and Figpack Slides?
* Getting started with Figpack Slides
* The main markdown file - index.md
* Rules for slides
* Tabs
* Font sizes
* Embedding images
* Embedding iframes
* Embedding external markdown files
* Custom Figpack views
* Customization
* Developing and building
* Hosting on GitHub Pages

---

# Figpack and Figpack Slides

### What is Figpack?

A Python package for interactive scientific visualization and data analysis.

* Exports figures as shareable, self-contained HTML
* Linked views in customizable dashboards
* Local or cloud storage options
* Handles large data via Zarr
* Built for neurophysiology, useful broadly

See [the documentation](https://flatironinstitute.github.io/figpack/) for more details.

* * *

### What is Figpack Slides?

A Figpack extension for creating interactive slide presentations, like this one!

This presentation will show you how to use Figpack Slides to create your own presentations.

---

# Getting Started with Figpack Slides

The first step is to copy (don't fork) this repository as a template for your own presentation.

Here's what you'll see in the template repository:

```bash
.github/workflows/  # GitHub Actions workflows for automatic deployment
build/              # Built presentation (auto-generated, don't edit)
images/             # Images used in the presentation
markdown_files/     # Additional markdown files for content
dev.sh              # Script to run in watch mode during development
index.md            # Main markdown file for the presentation
index.py            # Script to build the entire presentation
README.md           # About this repository
```

---

# The main markdown file - index.md

The index.md file serves as the backbone of your presentation. It contains the content of your slides, written in markdown format.

The content of this file is on the right side of this slide! So, you should be able to see how this slide in particular was constructed. :)

* * *

```yaml section-metadata
markdown-as-text: True
```

./index.md

---

# Rules for Slides

* Slides are separated by `---` lines.
* An optional slide type is specified at the top of each slide using the ````yaml slide-metadata ... ``` syntax.
* The content of each slide is split into one or more sections using `* * *` lines (three asterisks).
* Each section can contain metadata at the top, specified using the ````yaml section-metadata ... ``` syntax.
* If slide-type is "title", then the slide will expect subtitle and author metadata as well.
* By default, if two sections are present, the first will be on the left and the second on the right.
* If a section is a single `![alt text](image_path)` line, it will be treated as an image and sized to fill the section.
* If a section is a single `<iframe ...></iframe>` line, it will be treated as an iframe and will be sized to fill the section.
* If a section is a single `./path/to/file.md` line, it will be treated as a reference to an external markdown file and the contents of that file will be included in the section (scrollable).

---

# Tabs

```yaml slide-metadata
slide-type: tabs-on-right
```

This slide showcases the "tabs-on-right" slide type. In this case we have four sections. The first section corresponds to the main content on the left side. The other three sections correspond to tabs on the right side.

* * *

```yaml section-metadata
tab-label: Main
```

This is the first tab

* * *

```yaml section-metadata
tab-label: Tab 2
```

This is the second tab

* * *

```yaml section-metadata
tab-label: Tab 3
```

This is the third tab

---

# Font Sizes

```yaml slide-metadata
slide-type: tabs-on-right
```

Font sizes can be controlled using the following section metadata:

```yaml section-metadata
font-size: small | medium-small | medium | medium-large | large
```

The default font size is "medium".

See the tabs on the right for examples of different font sizes.

* * *

```yaml section-metadata
tab-label: Small
font-size: small
```

This is small font size.

* * *

```yaml section-metadata
tab-label: Medium-Small
font-size: medium-small
```

This is medium-small font size.

* * *

```yaml section-metadata
tab-label: Medium
font-size: medium
```

This is medium font size.

* * *

```yaml section-metadata
tab-label: Medium-Large
font-size: medium-large
```

This is medium-large font size.

* * *

```yaml section-metadata
tab-label: Large
font-size: large
```

This is large font size.

---

# Embedding Images

A remote image can be embedded in the markdown using the syntax

```
![alt text](image_url)
```

![Baby hamster](https://upload.wikimedia.org/wikipedia/commons/9/99/Babyhamster-scottobear.jpg)

---

# Embedding Local Images

A local image can be embedded using the syntax

```
![alt text](./images/image_filename.png)
```

Don't forget to include the "./" at the beginning of the path!

![A hamster and a hamster wheel](./images/A_hamster_and_a_hamster_wheel.jpeg)

---

# Embedding Local Images

If that local image is the only content in a section, it will be sized and centered according to the section size. For example, this slide contains only an image on the right side.

> Note: Make the browser window smaller to see how the image resizes.

* * *

![Baby hamster](./images/A_hamster_and_a_hamster_wheel.jpeg)

---

# Embedding Iframes

An iframe can be embedded in a section using the syntax

```
<iframe src="url"></iframe>
```

* * *

<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>

---

# Embedding External Markdown Files

A markdown file can be embedded in a section using the syntax

```
./path/to/file.md
```

That must be the only content in the section.

For example, this slide includes the contents of the file `./markdown_files/example_markdown.md` on the right side.

I got that file [from here](https://jaspervdj.be/lorem-markdownum/).

* * *

./markdown_files/example_markdown.md

---

# Custom Figpack Views

You can embed [arbitrary Figpack views](https://flatironinstitute.github.io/figpack) that are defined in Python.

In this case, the section on the right has no content, but it has metadata specifying a custom Figpack view.

Then, this is handled in the `create_slide.py` script to generate a custom Figpack view.

* * *

```yaml section-metadata
view-type: example-1
plot-color: "#00B000"
```

---

# Developing and Building

See the README.md file (to the right) for instructions on how to develop and build your presentation.

* * *

./README.md

---

# Hosting on GitHub Pages

Once you have your presentation built, you can host it on GitHub Pages for free.

1. Push this repository to GitHub.
2. In the repository settings, configure Pages so that it is built using GitHub Actions.

That's it! Your presentation will be automatically built and hosted on GitHub Pages whenever you push changes to the repository.



