import re

with open("engagement-models.html", "r") as f:
    content = f.read()

# Replace <title>
content = re.sub(r'<title>.*?</title>', '<title>Engagement Models | Kritox Digital</title>', content)

# Define replacement
replacement = """    <!-- Engagement Models Hero Section -->
    <section class="inner-hero border-b border-[#EDEDED] relative">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.1]">
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center relative z-10">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">How We Work</p>
                <h1 class="font-black tracking-tight leading-[1.05] mb-6 text-[2.5rem] md:text-[3.5rem] text-[#1F3D5A]">
                    Engagement <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Models.</span>
                </h1>
                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    We prioritize building enduring partnerships by providing flexible, risk-free, and rewarding engagement models. Our aim is to foster a collaborative environment where our expertise aligns with your needs, working together to accomplish your business objectives.
                </p>

                <div class="flex flex-wrap items-center gap-6 mt-8">
                    <a href="contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                        Consult Us <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                </div>
            </div>
            <div class="relative">
                <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=1000" alt="Engagement Models" class="rounded-[2rem] shadow-2xl w-full h-[400px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex items-center gap-4">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center shrink-0">
                        <i data-lucide="users" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <p class="text-[#1F3D5A] font-black text-xl">Flexible</p>
                        <p class="text-[#4A4A4A] text-sm font-medium">Hiring Models</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Engagement Models Detail Section -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">TAILORED TO YOUR NEEDS</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">
                    Evaluate Engagement Models We Offer
                </h2>
                <p class="text-lg text-[#4A4A4A] leading-relaxed max-w-3xl mx-auto">
                    We prioritize client flexibility, allowing you to engage and collaborate with us based on both immediate and long-term requirements. You have the freedom to choose a single model or combine multiple models to align precisely with your project demands.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Dedicated Development Team -->
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col group">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="users" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Dedicated Development Team</h3>
                    <p class="text-[#4A4A4A] text-sm mb-6 leading-relaxed">
                        A collaborative approach where you hire a group of skilled developers who work exclusively on your project. Ideal for projects that demand a high level of engagement, long-term commitment, and frequent changes.
                    </p>
                    <ul class="space-y-3 mb-8 flex-1 text-sm text-[#4A4A4A]">
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Tailor the team's size and skill sets</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Directly manage and oversee progress</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Seamless integration with in-house teams</li>
                    </ul>
                    <a href="contact.html" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm mt-auto w-full">
                        Hire a Team <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Time and Material -->
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col group">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="clock" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Time and Material (T&M)</h3>
                    <p class="text-[#4A4A4A] text-sm mb-6 leading-relaxed">
                        A dynamic strategy where clients pay for the actual time and resources invested. It suits endeavors where the scope, specifications, or deadlines are prone to alterations during development.
                    </p>
                    <ul class="space-y-3 mb-8 flex-1 text-sm text-[#4A4A4A]">
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Adaptable to changing project requirements</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Pay only for actual time/resources utilized</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Greater control to prioritize and modify</li>
                    </ul>
                    <a href="contact.html" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm mt-auto w-full">
                        Partner With Us <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Fixed Cost Model -->
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col group">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="briefcase" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Fixed Cost Model</h3>
                    <p class="text-[#4A4A4A] text-sm mb-6 leading-relaxed">
                        A structured approach where project scope, deliverables, and costs are predetermined. Suitable for projects with well-defined requirements and limited potential for scope changes.
                    </p>
                    <ul class="space-y-3 mb-8 flex-1 text-sm text-[#4A4A4A]">
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Financial predictability and budget planning</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Clearly outlined deliverables and deadlines</li>
                        <li class="flex items-start gap-2"><i data-lucide="check" class="w-4 h-4 text-[#2F6F73] mt-0.5 shrink-0"></i> Minimizes risks due to fixed scope</li>
                    </ul>
                    <a href="contact.html" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm mt-auto w-full">
                        Get Estimate <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Compare Models -->
    <section class="bg-brand-dark py-24 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tight">Engagement Models: A Comparative Overview</h2>
                <p class="text-lg text-white/90">Each engagement model has unique benefits for different business ideas. Here is a quick comparison to help you choose the best fit.</p>
            </div>
            
            <div class="overflow-x-auto rounded-3xl border border-white/10 bg-white/5 backdrop-blur-md">
                <table class="w-full min-w-[800px] text-left border-collapse">
                    <thead>
                        <tr class="border-b border-white/10 bg-white/5">
                            <th class="p-6 text-white font-bold text-lg">Aspects</th>
                            <th class="p-6 text-[#E5B93C] font-bold text-lg border-l border-white/10 w-1/4">Dedicated Team</th>
                            <th class="p-6 text-[#2F6F73] font-bold text-lg border-l border-white/10 w-1/4">Time & Material</th>
                            <th class="p-6 text-white font-bold text-lg border-l border-white/10 w-1/4">Fixed Cost</th>
                        </tr>
                    </thead>
                    <tbody class="text-white/80 text-sm">
                        <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                            <td class="p-6 font-semibold text-white">Project Scope</td>
                            <td class="p-6 border-l border-white/10">Flexible / Evolving</td>
                            <td class="p-6 border-l border-white/10">Flexible / Changing</td>
                            <td class="p-6 border-l border-white/10">Strictly Defined</td>
                        </tr>
                        <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                            <td class="p-6 font-semibold text-white">Cost & Budget</td>
                            <td class="p-6 border-l border-white/10">Monthly / Resource-based</td>
                            <td class="p-6 border-l border-white/10">Pay per hour/milestone</td>
                            <td class="p-6 border-l border-white/10">Fixed / Predetermined</td>
                        </tr>
                        <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                            <td class="p-6 font-semibold text-white">Project Manager</td>
                            <td class="p-6 border-l border-white/10">Optional / Available</td>
                            <td class="p-6 border-l border-white/10">Optional / Available</td>
                            <td class="p-6 border-l border-white/10">Included</td>
                        </tr>
                        <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                            <td class="p-6 font-semibold text-white">Best Suited For</td>
                            <td class="p-6 border-l border-white/10">Long-term projects, Core team extension</td>
                            <td class="p-6 border-l border-white/10">Iterative, Dynamic projects</td>
                            <td class="p-6 border-l border-white/10">Short-term, Clear requirements</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="mt-12 text-center">
                <a href="contact.html" class="inline-flex items-center gap-2 px-8 py-4 bg-[#E5B93C] text-brand-dark font-bold text-base rounded-2xl hover:brightness-110 transition-colors">
                    Consult Our Experts <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
            </div>
        </div>
    </section>
"""

start_idx = content.find('<!-- Services Hero Section -->')
end_idx = content.find('<!-- Footer -->')

new_content = content[:start_idx] + replacement + "\n" + content[end_idx:]

with open("engagement-models.html", "w") as f:
    f.write(new_content)
