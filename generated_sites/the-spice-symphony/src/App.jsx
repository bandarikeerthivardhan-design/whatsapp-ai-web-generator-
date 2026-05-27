import React from 'react';

const App = () => {
  const content = {"about_text": "At The Spice Symphony, we believe that food is a celebration of life. Founded with a passion for authentic culinary traditions, we source the finest ingredients and hand-ground spices to create a symphony of flavors on your plate.", "cta_text": "Reserve a Table", "feature_descriptions": ["A curated menu featuring rich, traditional recipes passed down through generations.", "Easily reserve your table online for an unforgettable dining experience.", "A warm, inviting ambiance perfect for family gatherings and romantic dinners."], "footer_text": "\u00a9 2024 The Spice Symphony. All rights reserved. Savor the tradition.", "hero_description": "Indulge in a culinary journey where traditional spices meet timeless elegance. Every dish at The Spice Symphony is a masterpiece crafted to delight your senses.", "hero_heading": "Experience the Harmony of Authentic Flavors"};
  const features = ["Online Reservation Table", "Interactive Digital Menu", "Customer Testimonials", "Photo Gallery"];
  const theme = "warm traditional";
  const isDark = theme.includes('dark');

  return (
    <div className={`min-h-screen ${isDark ? 'bg-slate-900 text-white' : 'bg-white text-gray-900'}`}>
      {/* Navigation */}
      <nav className="p-6 flex justify-between items-center border-b border-gray-700/50">
        <div className="flex items-center gap-2">
          <div className="w-10 h-10 bg-primary rounded-lg flex items-center justify-center text-white font-bold text-xl shadow-lg">
            T
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-primary">The Spice Symphony</h1>
        </div>
        <div className="space-x-6 hidden md:flex">
          
          <a href="#" className="hover:text-primary transition-colors capitalize">Home</a>
          
          <a href="#" className="hover:text-primary transition-colors capitalize">Menu</a>
          
          <a href="#" className="hover:text-primary transition-colors capitalize">About Us</a>
          
          <a href="#" className="hover:text-primary transition-colors capitalize">Reservations</a>
          
          <a href="#" className="hover:text-primary transition-colors capitalize">Contact</a>
          
        </div>
        <button className="bg-primary hover:opacity-90 text-white px-5 py-2 rounded-full font-medium transition-all">
          {content.cta_text}
        </button>
      </nav>

      {/* Hero Section */}
      <header className="py-20 px-6 text-center max-w-6xl mx-auto flex flex-col items-center">
        <div className="w-full max-w-3xl mb-12 rounded-3xl overflow-hidden shadow-2xl rotate-1">
          <img src="{data.hero_image}" alt="Hero" className="w-full h-80 object-cover" />
        </div>
        <div className="max-w-3xl">
          <h2 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
            {content.hero_heading}
          </h2>
          <p className="text-xl opacity-80 mb-10 leading-relaxed">
            {content.hero_description}
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <button className="bg-primary text-white px-8 py-4 rounded-xl text-lg font-bold shadow-lg hover:scale-105 transition-transform">
              {content.cta_text}
            </button>
            <button className="border border-gray-500 px-8 py-4 rounded-xl text-lg font-bold hover:bg-gray-500/10 transition-colors">
              Learn More
            </button>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="py-20 px-6 bg-black/5">
        <div className="max-w-6xl mx-auto">
          <h3 className="text-3xl font-bold text-center mb-16">Why Choose Us</h3>
          <div className="grid md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div key={index} className={`p-8 rounded-2xl border ${isDark ? 'bg-slate-800 border-gray-700' : 'bg-white border-gray-200'} shadow-sm hover:shadow-xl transition-shadow`}>
                <div className="w-12 h-12 bg-primary/20 rounded-lg flex items-center justify-center mb-6 text-primary">
                  <span className="font-bold text-xl">{index + 1}</span>
                </div>
                <h4 className="text-xl font-bold mb-3">{feature}</h4>
                <p className="opacity-70 leading-relaxed">
                  {content.feature_descriptions[index] || "We provide top-tier solutions tailored to your specific business needs and goals."}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-20 px-6 max-w-4xl mx-auto text-center">
        <h3 className="text-3xl font-bold mb-6">About The Spice Symphony</h3>
        <p className="text-lg opacity-80 leading-loose">
          {content.about_text}
        </p>
      </section>

      {/* Footer */}
      <footer className={`py-12 px-6 border-t ${isDark ? 'border-gray-800' : 'border-gray-200'}`}>
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
          <div>
            <h4 className="text-xl font-bold text-primary mb-2">The Spice Symphony</h4>
            <p className="opacity-60 max-w-xs">{content.footer_text}</p>
          </div>
          <div className="flex flex-col items-center md:items-end">
            <p className="font-medium">Contact Us</p>
            <p className="opacity-70">reservations@thespicesymphony.com</p>
            <p className="opacity-70">+1 (555) 234-5678</p>
          </div>
        </div>
        <div className="mt-12 pt-8 border-t border-gray-800/10 text-center opacity-40 text-sm">
          &copy; {new Date().getFullYear()} The Spice Symphony. All rights reserved.
        </div>
      </footer>
    </div>
  );
};

export default App;