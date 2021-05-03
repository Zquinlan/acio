---
layout: splash

header:
  overlay_color: "#5e616c"
  overlay_image: /assets/images/Coral_blue_tiny_fish_1.jpg
excerpt: >
  Academio to Io (AcIo): A static website generator for scientific github repositories <br /><br /><br />

feature_row:
  - image_path: /assets/images/about.jpg
    alt: "About"
    title: "About"
    excerpt: "What is AcIo?"
    url: "/about/"
    btn_class: "btn--primary"
    btn_label: "Learn more"
  - image_path: /assets/images/tutorial.png
    alt: "Tutorial"
    title: "Tutorial"
    excerpt: "How to use AcIo to generate your own github hosted website"
    url: "/tutorial/"
    btn_class: "btn--primary"
    btn_label: "Learn more"
  - image_path: /assets/images/contact.jpg
    alt: "contact us"
    title: "Contact Us!"
    excerpt: "Get involved, get help or post issues"
    url: "/contact/"
    btn_class: "btn--primary"
    btn_label: "See more"  
---

{% include feature_row %}

{% for post in site.posts limit: 5 %}
  {% include archive-single.html %}
{% endfor %}