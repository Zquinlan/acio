---
layout: splash

header:
  overlay_color: "#5e616c"
  overlay_image: /assets/images/Coral_blue_tiny_fish_1.jpg
excerpt: >
  Characterizing the micro members within coral reef ecosystems: Investigation of chemical and microbial diversity to understand shifting reef ecosystems.<br /><br /><br />

feature_row:
  - image_path: /assets/images/about.jpg
    alt: "About"
    title: "About"
    excerpt: "Who are we and what are we interested in studying!?"
    url: "/about/"
    btn_class: "btn--primary"
    btn_label: "Learn more"
  - image_path: /assets/images/labMembers.png
    alt: "Lab Members"
    title: "Lab Members"
    excerpt: "Current Lab members and their work"
    url: "/labMembers/"
    btn_class: "btn--primary"
    btn_label: "Learn more"
  - image_path: /assets/images/researchPhotos.jpg
    alt: "photos"
    title: "Photos!"
    excerpt: "See some of the photos from our research!"
    url: "/photos/moorea/"
    btn_class: "btn--primary"
    btn_label: "See more"  
---

{% include feature_row %}

{% for post in site.posts limit: 5 %}
  {% include archive-single.html %}
{% endfor %}