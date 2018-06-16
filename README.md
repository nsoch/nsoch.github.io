# Natacha Wild Dreamer

This is the future home natacha.net.

## Archive
The old site is provided here in [archive](archive). These files have not been 
touched or changed since download from (deprecated) natacha.net on 
June 13, 2018. The NKG Gallery site has been moved to a separate repository
at [nkg](https://www.github.com/vsoch/nkg).

## How does this work? 

The files live in a static Github repository, and they are rendered on 
[Github pages](https://pages.github.com/). Each repository has branches, and
we can configure Github pages to render the content from the master branch. The pages 
are rendered from markdown templates with an engine called Jekyll that results in
typical static html/css files. What makes jekyll really easy is that you can
write syntax that will (programatically) generate the files (e.g., so you can make
changes to one template and they propogate across the site). The cool thing about
Github pages is that it gives you web hosting, for free, and with https. It also
makes it really easy to update your site because you just make changes to the repository
on your local computer and then commit and push to Github. This means you do
need to familiarize yourself with the [Github flow to use it](https://guides.github.com/introduction/flow/).

## Introduction to Github
You must read about [Github flow](https://guides.github.com/introduction/flow/) before
any of this makes sense. You should understand the following concepts:

 - what a repository is
 - the difference between local and remote
 - branches and commits

and of course have a Github account! Once you do, you should fork this repository in
the web interface to your account, and then clone your fork. If your username is `vsoch`
the clone would look like this:

```bash
git clone https://www.github.com/vsoch/nsoch.github.io
cd nsoch.github.io
```

We will use [jekyll](https://jekyllrb.com/docs/quickstart/) to build and run a server.

```bash
bundle exec jekyll serve
```

## Making Changes
Generally, you will want to check out a new branch for your changes or new feature.

```bash
git checkout -b myfeature master
```

And then make the changes, and commit with a message.

```bash
git commit -a -m "This is a note about this change!"
```

Then you can push to your branch:

```bash
git push origin myfeature
```

And open a [pull request](https://help.github.com/articles/about-pull-requests/) in the web interface to the master branch when you are ready.


## How do I write a new blog post?
You should create a new file in the folder `_posts` (and put it inside a subdirectory that if appropriate)
that is named in this format:

```bash
_posts/poetry/YEAR-MONTH-DAY-TITLE.md
_posts/poetry/2018-06-13-resilient.md
```

You can create a directory if needed under `_posts`, all files here will be automatically rendered into posts, and the URL will capture the year and title (the folder organization is just for you, it doesn't impact the URL). For example, for the file above, the permalink (means permanent link) would be at `vsoch.github.io/nsoch.github.io/2018/resilient`

The top section of the file is called the front end matter, and you should generally modify the title
and categories, and your name.

```bash
---
layout: post
title: "Resilient"
author: "Vanessa Sochat"
categories: project
tags: [blog,thinking,poem]
---
```

Underneath that you can write whatever you like! The text under the `---` is the bulk of the post,
and it should be written in [Github flavored markdown](https://guides.github.com/features/mastering-markdown/). 

## How do I add a new project?

A project is a set of images associated with a page that you can write thoughts or
notes on. To create a new project, first:

**Add the project data**
Add an entry in [_data/projects.yml](_data/projects.yml). Just copy paste a previous one and write a project name. This name will correspond with the url (e.g., neuromorphic --> `nsoch.github.io/project/neuromorphic`) so keep this in mind. For example, let's look at this entry:

```bash
-
 title: Neuromorphic, 2011
 directory: neuromorphic
 image: 1.jpg
```

  - the project will have Title "Neuromorphic, 2011" and 
  - the URL will be at `nsoch.github.io/project/neuromorphic` (you largely don't need to worry about this, it will generate for you in the templates from here)
  - you will put images for the project in `assests/img/project/neuromorphic`
  - the image 1.jpg is expected to be in the folder above, and is a "banner image" for the project. 


**Add the images**
As mentioned above, you should put all your project images in a folder under `assets/img/project` that corresponds to the "directory" field above. You likely will need to create this folder!


**Add the project page**
The project itself is a markdown (a text file ending in .md) in the folder [projects](projects). This means that you can copy another project file and rename it! This markdown file should be named according to the same directory field above. So, for the directory:neuromorphic we would have:

```
projects/
  neuromorphic.md
```

What does the content in the file look like? It's pretty simple. There is a header section where you write a bunch of metadata, and then a content section that will have syntax to render the gallery. In the metadata section you will specify the list of images for the gallery to render. Here is a full example:

```yaml
---
layout: gallery
title: Uprooted
no_menu_item: true # required only for this example website because of menu construction
categories: project
tags: [uprooted]
image: uprooted/uprooted.jpg
support: [jquery, gallery]
picture_path: uprooted
preview:
- original: uprooted.jpg
pictures:
- original: uprooted.jpg
- original: root0.jpg
- original: root10.jpg
- original: root11.jpg
- original: root3.jpg
- original: root8.jpg
- original: root5.jpg
- original: root9.jpg
- original: root2.jpg
- original: root6.jpg
- original: root1.jpg
- original: root7.jpg
- original: root4.jpg
- original: backroot.jpg
---

> Beland Gallery Essex Art Center, Lawrence MA, June 17 - August 11, 2011

{% include gallery.html gallery=site.data.projects.uprooted %}
```

You can change the title, and tags, and "image" should correspond to the directory and then image name
that you want to render as the "main" gallery image. `picture_path` should correspond with `directory`
in the site metadata, an then `preview` should again be some primary image in your directory. The list of
images under `pictures` are the ones that will render in the gallery. I'm lazy, so I write a python script to
generate this for me, but you could do it manually.

```bash
python assets/scripts/generate_gallery.py assets/img/project/uprooted
```

Finally, you can add any notes or quoted content after the `---` and before the include
statement. For the include statement, you need to change the `gallery=site.data.projects.uprooted` to point
to the correct project. In our example, we would change that to `gallery=site.data.projects.neuromorphic`

## License

Open sourced under the [MIT license](LICENSE.md).
