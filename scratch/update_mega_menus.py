# [ignoring loop detection]
import os
import re

def get_desktop_technologies_menu(prefix):
    return f"""<!-- Technologies -->
                <div class="nav-item nav-item-full">
                    <button
                        class="nav-link-item flex items-center gap-1 py-2 px-3 text-[16px] text-neutral-dark font-semibold hover:text-brand-base transition-colors">
                        Technologies <i data-lucide="chevron-down" class="w-3 h-3"></i>
                    </button>
                    <div class="mega-menu-panel mega-menu-full bg-[#FAFAFA] border-b border-neutral-light py-6">
                        <div class="max-w-7xl mx-auto px-10 grid grid-cols-4 gap-0">
                            <div class="bg-brand-dark rounded-2xl p-7 mr-6 flex flex-col justify-between min-h-[200px]">
                                <div>
                                    <p class="text-white font-black text-2xl leading-snug mb-3">Tech that Scales</p>
                                    <p class="text-teal-50 text-[14px] leading-relaxed">Modern stack for modern businesses.</p>
                                </div>
                                <a href="{prefix}contact.html" class="btn-quote-sm">Consult Experts <span
                                        class="btn-quote-sm-icon"><i data-lucide="arrow-right"
                                            class="w-3 h-3"></i></span></a>
                            </div>
                            <!-- Column 1: Design & Mobile -->
                            <div class="flex flex-col justify-between pr-6 border-r border-[#EDEDED]">
                                <div class="flex flex-col gap-2">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Design</p>
                                    <a href="{prefix}tech/web-design.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="monitor" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Web Design</p>
                                    </a>
                                    <a href="{prefix}tech/uiux.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="layout" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">UI/UX</p>
                                    </a>
                                    <a href="{prefix}tech/brand-design.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="pen-tool" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Brand Design</p>
                                    </a>
                                </div>
                                <div class="flex flex-col gap-2 mt-4 pt-4 border-t border-[#EDEDED]/50">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Mobile</p>
                                    <a href="{prefix}tech/mobile.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="smartphone" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">React Native & Flutter</p>
                                    </a>
                                    <a href="{prefix}tech/ios.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="smartphone" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">iOS</p>
                                    </a>
                                    <a href="{prefix}tech/android.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="smartphone" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Android</p>
                                    </a>
                                </div>
                            </div>
                            <!-- Column 2: Web & eCommerce -->
                            <div class="flex flex-col justify-between px-6 border-r border-[#EDEDED]">
                                <div class="flex flex-col gap-2">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Web</p>
                                    <a href="{prefix}tech/wordpress.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="layout-template" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">WordPress</p>
                                    </a>
                                    <a href="{prefix}tech/php.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="server" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">PHP</p>
                                    </a>
                                    <a href="{prefix}tech/laravel.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="server" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Laravel</p>
                                    </a>
                                    <a href="{prefix}tech/react.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="code" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">React.js</p>
                                    </a>
                                    <a href="{prefix}tech/vue.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="code" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Vue.js</p>
                                    </a>
                                    <a href="{prefix}tech/angular.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="code" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Angular.js</p>
                                    </a>
                                    <a href="{prefix}tech/node.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="server" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Node.js</p>
                                    </a>
                                    <a href="{prefix}tech/python.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="terminal" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Python</p>
                                    </a>
                                </div>
                                <div class="flex flex-col gap-2 mt-4 pt-4 border-t border-[#EDEDED]/50">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">eCommerce</p>
                                    <a href="#" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="shopping-cart" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Magento</p>
                                    </a>
                                    <a href="#" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="shopping-bag" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Shopify</p>
                                    </a>
                                    <a href="#" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="shopping-cart" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">WooCommerce</p>
                                    </a>
                                </div>
                            </div>
                            <!-- Column 3: Data & Integrations and Cloud & DevOps -->
                            <div class="flex flex-col justify-between pl-6">
                                <div class="flex flex-col gap-2">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Data & Integrations</p>
                                    <a href="{prefix}tech/databases.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="database" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">MongoDB</p>
                                    </a>
                                    <a href="{prefix}tech/databases.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="database" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">MySQL</p>
                                    </a>
                                    <a href="{prefix}tech/databases.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="database" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">PostgreSQL</p>
                                    </a>
                                    <a href="#" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="link" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">APIs & Messaging</p>
                                    </a>
                                </div>
                                <div class="flex flex-col gap-2 mt-4 pt-4 border-t border-[#EDEDED]/50">
                                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Cloud & DevOps</p>
                                    <a href="{prefix}tech/aws.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="cloud" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">AWS & GCP</p>
                                    </a>
                                    <a href="{prefix}tech/ai.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="cpu" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">AI & ML</p>
                                    </a>
                                    <a href="{prefix}tech/docker.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="box" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Docker & K8s</p>
                                    </a>
                                    <a href="{prefix}tech/cicd.html" class="group flex gap-3 items-center">
                                        <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]">
                                            <i data-lucide="git-branch" class="w-3 h-3"></i>
                                        </div>
                                        <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">CI/CD & DevOps</p>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>"""

def get_mobile_technologies_menu(prefix):
    return f"""<details class="group border-b border-[#EDEDED] pb-4">
                <summary
                    class="flex items-center justify-between text-xl font-bold text-[#1F3D5A] cursor-pointer list-none">
                    Technologies
                    <i data-lucide="chevron-down"
                        class="w-5 h-5 text-[#4A4A4A] transition-transform group-open:rotate-180"></i>
                </summary>
                <div class="mt-3 space-y-2 pl-1">
                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Design</p>
                    <a href="{prefix}tech/web-design.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Web Design</a>
                    <a href="{prefix}tech/uiux.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">UI/UX</a>
                    <a href="{prefix}tech/brand-design.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Brand Design</a>

                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Web</p>
                    <a href="{prefix}tech/wordpress.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">WordPress</a>
                    <a href="{prefix}tech/php.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">PHP</a>
                    <a href="{prefix}tech/laravel.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Laravel</a>
                    <a href="{prefix}tech/react.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">React.js</a>
                    <a href="{prefix}tech/vue.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Vue.js</a>
                    <a href="{prefix}tech/angular.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Angular.js</a>
                    <a href="{prefix}tech/node.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Node.js</a>
                    <a href="{prefix}tech/python.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Python</a>

                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Mobile</p>
                    <a href="{prefix}tech/mobile.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">React Native & Flutter</a>
                    <a href="{prefix}tech/ios.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">iOS</a>
                    <a href="{prefix}tech/android.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Android</a>

                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">eCommerce</p>
                    <a href="#"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Magento</a>
                    <a href="#"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Shopify</a>
                    <a href="#"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">WooCommerce</a>

                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Data & Integrations</p>
                    <a href="{prefix}tech/databases.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">MongoDB</a>
                    <a href="{prefix}tech/databases.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">MySQL</a>
                    <a href="{prefix}tech/databases.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">PostgreSQL</a>
                    <a href="#"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">APIs & Messaging</a>

                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Cloud & DevOps</p>
                    <a href="{prefix}tech/aws.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">AWS & GCP</a>
                    <a href="{prefix}tech/ai.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">AI & ML</a>
                    <a href="{prefix}tech/docker.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Docker & K8s</a>
                    <a href="{prefix}tech/cicd.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">CI/CD & DevOps</a>
                </div>
            </details>"""

def main():
    root_dir = "/Users/devshrimali/Documents/Work/AEC/kritox-digi"
    
    # We will search and replace in all HTML files in the workspace
    for dirpath, _, filenames in os.walk(root_dir):
        if ".git" in dirpath or "node_modules" in dirpath:
            continue
            
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
                
            filepath = os.path.join(dirpath, filename)
            
            # Determine prefix
            rel_path = os.path.relpath(filepath, root_dir)
            parts = rel_path.split(os.sep)
            if len(parts) == 1:
                prefix = ""
            elif len(parts) == 2:
                prefix = "../"
            else:
                prefix = "../" * (len(parts) - 1)
                
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            
            # Match 1: Desktop Technologies mega menu replacement
            # Match from <!-- Technologies --> to </div>\s*</div>\s*</div>\s*</div>
            desktop_regex = r"<!-- Technologies -->\s*<div class=\"nav-item nav-item-full\">.*?Consult Experts.*?\n\s*</div>\s*</div>\s*</div>\s*</div>"
            new_desktop = get_desktop_technologies_menu(prefix)
            content = re.sub(desktop_regex, new_desktop, content, flags=re.DOTALL | re.IGNORECASE)
            
            # Match 2: Mobile Technologies submenu replacement
            # Match <details class="group border-b border-[#EDEDED] pb-4">\s*<summary[^>]*>\s*Technologies.*?</details>
            mobile_regex = r"<details class=\"group border-b border-\[#EDEDED\] pb-4\">\s*<summary[^>]*>\s*Technologies.*?</details>"
            new_mobile = get_mobile_technologies_menu(prefix)
            content = re.sub(mobile_regex, new_mobile, content, flags=re.DOTALL | re.IGNORECASE)
            
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated mega menu & mobile menu in: {rel_path}")

if __name__ == "__main__":
    main()
