// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/portfolio/";
    },
  },{id: "nav-my-games",
          title: "my games",
          description: "A growing collection of my game related projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/portfolio/games/";
          },
        },{id: "nav-data-projects",
          title: "data projects",
          description: "A growing collection of projects in gaming and various programming languages. Seperated currently by &quot;Games&quot;, &quot;Python&quot;, and &quot;Ruby&quot; sections.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/portfolio/projects/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "A look at the repo behind this page and my other github projects. Stats are pulled by a javascript repo and hosted on Vercel for real time pulling of data.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/portfolio/repositories/";
          },
        },{id: "nav-experience",
          title: "experience",
          description: "Click on the icon to the right to see my Resume. Refer to the below to see futher details on my experience.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/portfolio/resume/";
          },
        },{id: "dropdown-bookshelf",
              title: "bookshelf",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/portfolio/books/";
              },
            },{id: "dropdown-blog",
              title: "blog",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/portfolio/blog/";
              },
            },{id: "dropdown-about-me",
              title: "about me",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/portfolio/about_me/";
              },
            },{id: "dropdown-site-analytics",
              title: "site analytics",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/portfolio/analytics/";
              },
            },{id: "dropdown-fun-facts",
              title: "fun facts",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/portfolio/facts/";
              },
            },{id: "books-the-alchemist",
          title: 'The Alchemist',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/portfolio/books/alchemist/";
            },},{id: "books-babel",
          title: 'Babel',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/portfolio/books/babel/";
            },},{id: "books-dune",
          title: 'Dune',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/portfolio/books/dune/";
            },},{id: "books-the-great-gatsby",
          title: 'The Great Gatsby',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/portfolio/books/gatsby/";
            },},{id: "books-wizzywig-portrait-of-a-serial-hacker",
          title: 'Wizzywig, Portrait of a serial hacker',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/portfolio/books/wizzywig/";
            },},{id: "news-release-of-portfolio-2-0-current-site",
          title: 'Release of portfolio 2.0 (Current Site)',
          description: "",
          section: "News",},{id: "news-started-development-of-my-3d-unity-game-roll-a-ball",
          title: 'Started development of my 3D Unity game Roll-a-Ball',
          description: "",
          section: "News",},{id: "news-release-of-a-playable-demo-of-asteroid-survivors",
          title: 'Release of a playable demo of Asteroid Survivors',
          description: "",
          section: "News",},{id: "projects-first-ruby-jekyll-portfolio-site",
          title: 'First Ruby | Jekyll Portfolio Site',
          description: "Original portfolio site using Ruby&#39;s Jekyll site generator",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/first_port_site/";
            },},{id: "projects-machine-learning-via-tweets",
          title: 'Machine Learning via Tweets 🤖 🧠',
          description: "Training a model and creating a visualization based on Confidence score of the model using tweets from dataset from UIUC Data Science course.",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/machine_learning/";
            },},{id: "projects-network-clustering-analysis",
          title: '📊 Network Clustering Analysis',
          description: "Python project utilizing networkx",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/network_visual_project/";
            },},{id: "projects-python-interactive-data-visualization",
          title: '📊 Python Interactive Data Visualization',
          description: "Using Python and packages like Altair | Data Analytics | Data Visualization",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/python_data_viz/";
            },},{id: "projects-geo-plotting-analysis",
          title: '📊 Geo Plotting / Analysis',
          description: "Using python libraries to use data over geo maps",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/spatial_analysis/";
            },},{id: "projects-tei-solutions",
          title: '📊 TEI Solutions',
          description: "Converting HTML data to TEI | Data Parsing",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/tei_solutions/";
            },},{id: "projects-text-analysis-using-named-entity-recognition",
          title: '📊 Text Analysis using Named Entity Recognition',
          description: "Sorting through text using strategies like Named Entity Recognition and POS Tagging",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/text_analysis_ner/";
            },},{id: "projects-topic-modeling",
          title: '📊 Topic Modeling',
          description: "Topic Modeling with Python",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/topic_modeling/";
            },},{id: "projects-text-analysis-visualization",
          title: '📊 Text Analysis Visualization',
          description: "Python project | Data Scraping | Altair",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/video_essay_visualization/";
            },},{id: "projects-text-analysis-using-named-entity-recognition",
          title: '📊 Text Analysis using Named Entity Recognition',
          description: "Project using webscraped data using pandas and APIs.",
          section: "Projects",handler: () => {
              window.location.href = "/portfolio/projects/web_scraping/";
            },},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/portfolio/assets/pdf/resume.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%63%6F%6C%74%6F%6E.%64%65%76%30%32@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'Linkedin',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/colton-keiser/", "_blank");
        },
      },{
        id: 'social-repo',
        title: 'Repo',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/ckeiser2/portfolio", "_blank");
        },
      },{
        id: 'social-game',
        title: 'Game',
        section: 'Socials',
        handler: () => {
          window.open("https://ckeiser2.github.io/portfolio/games/asteroid_survivors/", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
