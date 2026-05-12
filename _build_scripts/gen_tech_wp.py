import os, re

ROOT = "/Users/devshrimali/Documents/Work/AEC/kritox-digi"
with open(f"{ROOT}/tech/wordpress.html") as f:
    WP = f.read()

PAGES = [
  ("react.html","React.js","Frontend Engineering","Build blazing-fast UIs with React.js — the industry standard for modern web apps.","Custom React Solutions","https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&q=80","code",
   [("Component Architecture","Build modular, reusable React components for scalable UIs."),("State Management","Redux, Zustand & Context API implementations."),("Next.js Development","SSR, SSG & ISR for production-grade React apps."),("API Integration","RESTful & GraphQL integrations with React Query."),("Performance Optimisation","Code splitting, lazy loading & Core Web Vitals."),("Testing & QA","Jest, React Testing Library & E2E with Playwright."),("Migration to React","Move legacy codebases to modern React architecture."),("UI Component Libraries","Custom design system & Storybook integration."),("React Native","Cross-platform mobile from your React web codebase.")]),
  ("vue.html","Vue.js","Frontend Engineering","Progressive, approachable Vue.js development for modern web applications.","Custom Vue Solutions","https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80","code",
   [("Vue 3 Composition API","Modern reactive logic with Vue 3 & Composition API."),("Nuxt.js Apps","SSR & static site generation with Nuxt.js."),("Pinia State Management","Lightweight & intuitive store management."),("Component Libraries","Custom Vue components & design systems."),("API Integration","Axios, REST & GraphQL with Vue."),("Performance Tuning","Lazy loading & bundle optimisation."),("Migration to Vue","Move legacy jQuery or AngularJS to Vue 3."),("Testing","Vitest & Vue Test Utils coverage."),("PWA with Vue","Offline-capable progressive web apps.")]),
  ("angular.html","Angular","Frontend Engineering","Enterprise-grade Angular development for scalable, robust web applications.","Custom Angular Solutions","https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&q=80","code",
   [("Angular 17+ Apps","Latest Angular with standalone components & signals."),("RxJS & State","NgRx & complex reactive state management."),("Module Architecture","Feature-module design for large-scale apps."),("REST & GraphQL","HttpClient & Apollo integration."),("Performance","Lazy modules, OnPush & zone-less apps."),("Testing","Jasmine, Karma & Cypress E2E."),("Migration","AngularJS to Angular 17 upgrades."),("Material UI","Angular Material & CDK component systems."),("Micro Frontends","Module Federation with Angular.")]),
  ("node.html","Node.js","Backend Engineering","High-performance Node.js APIs & microservices that scale.","Custom Node Solutions","https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&q=80","server",
   [("REST API Development","Scalable Express & Fastify REST APIs."),("GraphQL APIs","Apollo Server & schema-first API design."),("Microservices","Node.js microservice architecture with Docker."),("Real-time Apps","WebSocket & Socket.io integrations."),("Authentication","JWT, OAuth2 & session-based auth."),("Database Integration","MongoDB, PostgreSQL & Redis."),("Performance Tuning","Clustering, caching & profiling."),("Serverless Node","AWS Lambda & Vercel edge functions."),("API Gateway","Rate limiting, versioning & documentation.")]),
  ("python.html","Python","Backend Engineering","Python development for web, AI, automation and data engineering.","Custom Python Solutions","https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&q=80","terminal",
   [("Django Development","Full-featured web apps with Django ORM."),("FastAPI Services","High-performance async REST APIs."),("Data Engineering","Pandas, NumPy & ETL pipelines."),("AI & ML Integration","Scikit-learn, TensorFlow & LangChain."),("Web Scraping","Scrapy & Playwright automation."),("Automation Scripts","Task automation & workflow scripts."),("REST & GraphQL","Strawberry & Graphene APIs."),("Testing","Pytest & coverage automation."),("Deployment","Docker, CI/CD & Heroku/AWS.")]),
  ("php.html","PHP","Backend Engineering","Robust PHP development powering dynamic, high-traffic websites.","Custom PHP Solutions","https://images.unsplash.com/photo-1599507593499-a3f7d1d08731?auto=format&fit=crop&q=80","server",
   [("Custom PHP Apps","Bespoke PHP 8.x applications."),("Laravel Development","MVC apps with Laravel & Eloquent ORM."),("API Development","RESTful APIs with Lumen & Laravel."),("CMS Development","WordPress & custom PHP CMSs."),("Database Design","MySQL & PostgreSQL schema design."),("Performance","OPcache, query optimisation & CDN."),("Security","XSS, CSRF & SQL injection hardening."),("Testing","PHPUnit & Pest test coverage."),("Migration","Legacy PHP to modern frameworks.")]),
  ("laravel.html","Laravel","Backend Engineering","Laravel development — elegant, expressive and production-ready.","Custom Laravel Solutions","https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80","server",
   [("Laravel Apps","Full-stack apps with Blade & Livewire."),("REST APIs","Laravel Sanctum & Passport APIs."),("Queue Systems","Laravel Horizon & Redis queues."),("Eloquent ORM","Complex relationships & query optimisation."),("Multi-tenancy","Tenant-per-schema SaaS apps."),("Laravel Octane","High-performance Swoole/RoadRunner."),("Testing","Feature & unit tests with Pest."),("Deployment","Forge, Vapor & Docker CI/CD."),("Migration","Legacy apps to Laravel.")]),
  ("ios.html","iOS","Mobile Engineering","Native iOS apps crafted with Swift — beautiful, fast and App Store ready.","Custom iOS Solutions","https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&q=80","smartphone",
   [("Swift Development","SwiftUI & UIKit native iOS apps."),("App Store Launch","Full submission & ASO strategy."),("Push Notifications","APNs & rich notification experiences."),("Core Data & CloudKit","Offline-first data sync."),("ARKit & CoreML","Augmented reality & on-device AI."),("In-App Purchases","StoreKit 2 subscriptions & payments."),("Testing","XCTest & TestFlight beta distribution."),("App Maintenance","iOS version upgrades & bug fixes."),("Apple Watch","WatchKit companion app development.")]),
  ("android.html","Android","Mobile Engineering","Native Android apps built with Kotlin — performant, polished and Google Play ready.","Custom Android Solutions","https://images.unsplash.com/photo-1607252656733-fd7427926e5e?auto=format&fit=crop&q=80","smartphone",
   [("Kotlin Development","Modern Android with Jetpack Compose."),("Google Play Launch","Full submission & metadata optimisation."),("Firebase Integration","Auth, Firestore & Analytics."),("Room Database","Offline-first local data storage."),("Push Notifications","FCM & rich notifications."),("Google Maps & Location","Maps SDK & geofencing."),("Testing","Espresso & UI Automator."),("Android TV & Wear","Extended platform development."),("App Maintenance","Android version upgrades.")]),
  ("mobile.html","React Native & Flutter","Mobile Engineering","Cross-platform mobile apps — one codebase, two platforms, native performance.","Cross-Platform Solutions","https://images.unsplash.com/photo-1512428559087-560552a1d9ab?auto=format&fit=crop&q=80","smartphone",
   [("React Native Apps","Near-native iOS & Android from one JS codebase."),("Flutter Development","Dart-powered pixel-perfect cross-platform apps."),("App Store Submission","iOS & Android store launch & ASO."),("Push Notifications","Firebase & OneSignal integrations."),("Offline Support","AsyncStorage & SQLite sync."),("Navigation","React Navigation & Go Router."),("State Management","Redux Toolkit & Riverpod."),("Testing","Detox & Flutter integration tests."),("Performance","Hermes engine & tree shaking.")]),
  ("brand-design.html","Brand Design","Design Engineering","Strategic brand identity that makes your business unforgettable.","Custom Brand Solutions","https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80","pen-tool",
   [("Logo Design","Timeless, versatile logo mark creation."),("Brand Identity Systems","Color palettes, typography & guidelines."),("Brand Strategy","Positioning, messaging & tone of voice."),("Stationery Design","Business cards, letterheads & brand assets."),("Social Media Kits","Templates for consistent social presence."),("Packaging Design","Product & packaging visual identity."),("Brand Audit","Review & refresh of existing brand assets."),("Rebranding","Full rebrand strategy & execution."),("Pitch Decks","Investor-ready branded presentations.")]),
  ("uiux.html","UI/UX Design","Design Engineering","User-centered design that converts visitors into loyal customers.","Custom UI/UX Solutions","https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&q=80","layout",
   [("UX Research","User interviews, surveys & journey mapping."),("Wireframing","Low-fidelity wireframes & site maps."),("UI Design","High-fidelity pixel-perfect Figma designs."),("Prototyping","Interactive clickable prototypes."),("Design Systems","Component libraries & style guides."),("Usability Testing","A/B testing & heatmap analysis."),("Accessibility","WCAG 2.1 AA compliance audits."),("App Design","iOS & Android UI following platform HIG."),("Design Handoff","Dev-ready Zeplin & Figma specs.")]),
  ("web-design.html","Web Design","Design Engineering","Stunning, conversion-optimised website design for any industry.","Custom Web Design","https://images.unsplash.com/photo-1547658719-da2b51169166?auto=format&fit=crop&q=80","monitor",
   [("Landing Pages","High-converting campaign & product pages."),("Corporate Websites","Professional multi-page brand sites."),("E-commerce Design","Shopify & WooCommerce store design."),("Responsive Design","Flawless on all devices & screen sizes."),("CMS Integration","WordPress, Webflow & Contentful."),("UI Component Libraries","Reusable design component sets."),("Website Redesign","Refresh of existing underperforming sites."),("Speed Optimisation","Core Web Vitals & PageSpeed tuning."),("SEO-Friendly Structure","Architecture built for search visibility.")]),
  ("aws.html","AWS & Cloud","Backend Engineering","Reliable, secure AWS cloud architecture for modern digital products.","Custom Cloud Solutions","https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80","cloud",
   [("AWS Architecture","Scalable multi-tier cloud architectures."),("EC2 & ECS","Compute & container workload management."),("Serverless & Lambda","Event-driven cost-effective backends."),("S3 & CloudFront","Static hosting & global CDN delivery."),("RDS & DynamoDB","Managed relational & NoSQL databases."),("Security & IAM","Roles, policies & compliance audits."),("Cost Optimisation","Reserved instances & right-sizing."),("CI/CD on AWS","CodePipeline & GitHub Actions."),("Cloud Migration","On-premise to AWS lift & shift.")]),
  ("docker.html","Docker & Kubernetes","Backend Engineering","Containerise, orchestrate and ship software with confidence.","Container Solutions","https://images.unsplash.com/photo-1605745341112-85968b19335b?auto=format&fit=crop&q=80","box",
   [("Docker Setup","Containerise any application stack."),("Docker Compose","Multi-service local dev environments."),("Kubernetes Clusters","K8s cluster provisioning & management."),("Helm Charts","Packaging & deploying K8s applications."),("Container Security","Image scanning & runtime policies."),("Auto-scaling","HPA & cluster autoscaler setup."),("Monitoring","Prometheus, Grafana & alerting."),("Service Mesh","Istio & Linkerd for microservices."),("Migration to K8s","Move VMs to containerised workloads.")]),
  ("cicd.html","CI/CD & DevOps","Backend Engineering","Automate your release pipeline — ship faster, break less.","DevOps Solutions","https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&q=80","git-branch",
   [("GitHub Actions","Custom CI/CD workflows in GitHub."),("GitLab CI","Multi-stage pipelines in GitLab."),("Jenkins Setup","Enterprise Jenkins pipeline configuration."),("Infrastructure as Code","Terraform & Pulumi automation."),("Blue/Green Deployments","Zero-downtime production deployments."),("Environment Management","Dev, staging & prod parity."),("Automated Testing","Unit, integration & E2E in pipeline."),("Secrets Management","Vault & AWS Secrets Manager."),("Monitoring & Alerts","PagerDuty & Slack integrations.")]),
  ("databases.html","Databases","Backend Engineering","Database design, optimisation and management for any scale.","Database Solutions","https://images.unsplash.com/photo-1544383835-bda2bc66a55d?auto=format&fit=crop&q=80","database",
   [("PostgreSQL","Advanced relational DB design & tuning."),("MongoDB","Document store schema design & indexing."),("Redis","Caching, pub/sub & session stores."),("MySQL / MariaDB","High-availability MySQL setups."),("Database Migration","Safe schema migrations & data transfers."),("Query Optimisation","Index tuning & slow query analysis."),("Replication & HA","Master-replica & clustering setups."),("Backup & Recovery","Automated backup & PITR strategies."),("Database Auditing","Security & compliance reviews.")]),
]

WHY_ICONS = ["credit-card","pen-tool","search","smartphone","layout-dashboard","users","blocks","trending-up"]
WHY_COLORS = ["#E5B93C","#2F6F73","#1F3D5A","#E5B93C","#2F6F73","#1F3D5A","#E5B93C","#2F6F73"]

def why_cards(name):
    items = [
        (f"Proven {name} Experts","Vetted engineers with 5+ years of hands-on experience."),
        ("Agile Delivery","2-week sprints, daily standups & transparent reporting."),
        ("On-Time Launch","Milestone-based delivery with full accountability."),
        ("Scalable Solutions","Built to grow — from MVP to enterprise scale."),
        ("24/7 Support","Post-launch maintenance & rapid response SLA."),
        ("Transparent Pricing","Fixed-cost or T&M — no hidden fees ever."),
        ("IP Protection","Full NDA & intellectual property assignment."),
        ("UK & Global Clients","Trusted by 100+ businesses across 20+ countries."),
    ]
    cards = ""
    for i,(t,d) in enumerate(items):
        bg = "bg-[#FAFAFA]" if i%2==0 else "bg-white"
        icon = WHY_ICONS[i%8]
        color = WHY_COLORS[i%8]
        cards += f'''
                <div class="{bg} border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="{icon}" class="w-8 h-8 mb-4" style="color:{color}"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">{t}</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">{d}</p>
                </div>'''
    return cards

def service_cards(services):
    cards = ""
    for t,d in services:
        cards += f'''
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">{t}</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">{d}</p>
                </div>'''
    return cards

STEPS = [("Discovery","We understand your requirements, goals & technical constraints."),
         ("Planning","Architecture design, tech stack selection & roadmap."),
         ("Development","Agile sprints with daily updates & code reviews."),
         ("Testing","QA, performance & security testing before launch."),
         ("Launch","Deployment, monitoring & post-launch support.")]

def process_steps():
    s = ""
    for i,(t,d) in enumerate(STEPS,1):
        s += f'''
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">{i}</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">{t}</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">{d}</p>
                </div>'''
    return s

for fname,name,cat,desc,hero_label,img,icon,services in PAGES:
    html = WP

    # Title
    html = re.sub(r'<title>.*?</title>', f'<title>{name} Development Services | Kritox Digital</title>', html)

    # Hero label
    html = html.replace("Custom WordPress Solutions", hero_label)

    # Hero h1
    html = re.sub(r'WordPress <span class="text-transparent[^"]*"[^>]*>Development\.</span>', f'{name} <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Development.</span>', html)

    # Hero description
    html = html.replace("Want to launch a 100% responsive WordPress website? We're a bespoke and trusted WordPress development agency helping clients to launch a website with ease. Our custom solutions perform and grow with your business.", desc)

    # Hero image
    html = re.sub(r'https://images\.unsplash\.com/photo-1555066931-4365d14bab8c\?auto=format[^"]*', img, html)

    # Hero badge icon + label
    html = re.sub(r'data-lucide="layout-template"', f'data-lucide="{icon}"', html, count=1)
    html = html.replace("<p class=\"text-[#1F3D5A] font-black text-xl\">Trusted</p>", f'<p class="text-[#1F3D5A] font-black text-xl">{cat.split()[0]}</p>')
    html = html.replace("<p class=\"text-[#4A4A4A] text-sm font-medium\">Bespoke Agency</p>", f'<p class="text-[#4A4A4A] text-sm font-medium">{cat}</p>')

    # Why Choose section
    html = re.sub(r'Why Choose <span class="text-\[#2F6F73\]">WordPress\?</span>', f'Why Choose <span class="text-[#2F6F73]">{name}?</span>', html)
    html = html.replace("WordPress is trusted by millions of brand owners worldwide. Whatever you're looking for, WordPress provides you with complete flexibility.", f"{name} is trusted by leading businesses worldwide. Whatever your project requires, our {name} experts deliver with precision and speed.")
    # Replace why cards grid
    old_grid_start = '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">'
    old_grid_end = '</div>\n        </div>\n    </section>\n\n    <!-- WordPress Services Section'
    new_grid = f'{old_grid_start}{why_cards(name)}\n            </div>\n        </div>\n    </section>\n\n    <!-- {name} Services Section'
    html = html.replace(old_grid_start + html.split(old_grid_start,1)[1].split(old_grid_end,1)[0] + old_grid_end, new_grid, 1) if old_grid_start in html else html

    # Services section heading
    html = re.sub(r'<span class="text-brand-base">Bespoke</span> WordPress<br>Development Services\.', f'<span class="text-brand-base">Bespoke</span> {name}<br>Development Services.', html)
    html = html.replace("Whether you are creating a new website or looking to improve an existing one, check our white-label services to find exactly what you need.", f"Whether you need a new {name} project or want to enhance an existing one, explore our full range of {name} services below.")

    # Replace service cards grid
    svc_start = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
    svc_end = '</div>\n        </div>\n    </section>\n\n    <!-- Process Section'
    new_svc = f'{svc_start}{service_cards(services)}\n            </div>\n        </div>\n    </section>\n\n    <!-- Process Section'
    html = html.replace(svc_start + html.split(svc_start,1)[1].split(svc_end,1)[0] + svc_end, new_svc, 1) if svc_start in html else html

    # Process section heading
    html = re.sub(r'Our WordPress <span class="text-brand-base">Process</span>', f'Our {name} <span class="text-brand-base">Process</span>', html)
    html = html.replace("We understand your custom needs and deliver a tool that works smoothly.", f"We follow a proven process to deliver your {name} project on time and to spec.")

    # Replace process steps
    proc_start = '<div class="grid md:grid-cols-5 gap-5">'
    proc_end = '</div>\n        </div>\n    </section>\n\n    <!-- CTA Section'
    new_proc = f'{proc_start}{process_steps()}\n            </div>\n        </div>\n    </section>\n\n    <!-- CTA Section'
    html = html.replace(proc_start + html.split(proc_start,1)[1].split(proc_end,1)[0] + proc_end, new_proc, 1) if proc_start in html else html

    # CTA
    html = html.replace("Ongoing Maintenance", f"{name} Projects")
    html = html.replace("Let's discuss your project.", f"Ready to build with {name}?")
    html = html.replace("First impressions turn traffic into revenue. Our designers and developers will help you impress visitors and turn them into loyal customers.", f"Our {name} experts are ready to scope, build and ship your project. Get a free consultation today.")

    out = f"{ROOT}/tech/{fname}"
    with open(out,"w") as f:
        f.write(html)
    print(f"  ✓ {fname}")

print("Done — 17 tech pages rebuilt.")
