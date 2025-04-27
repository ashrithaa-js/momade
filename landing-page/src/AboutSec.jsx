import React, { useState } from "react";
import "./index.css";
import floatingImg3 from "./images/float3.png";
import floatingImg7 from "./images/float7.png";
import floatingImg5 from "./images/float5.png";

const AboutUs = () => {
  const videos = [
    "https://www.youtube.com/embed/dQw4w9WgXcQ", // Video 1
    "https://www.youtube.com/embed/3JZ_D3ELwOQ", // Video 2
  ];

  const [currentVideo, setCurrentVideo] = useState(0);

  const nextVideo = () => {
    setCurrentVideo((prev) => (prev + 1) % videos.length);
  };

  const prevVideo = () => {
    setCurrentVideo((prev) => (prev - 1 + videos.length) % videos.length);
  };

  return (
    <section className="section landing-section about-section" id="about">
      <div className="about-content">
        <div className="about-text">
          <h2>About Us</h2>
          <p>
            We’re more than just a food delivery service. We’re a community of
            passionate home chefs who pour their hearts into every dish,
            ensuring you enjoy the rich, authentic flavors of homemade cooking.
            Whether you're craving comfort food, festive delicacies, or healthy
            home-style meals, we have something special for everyone.<br></br>
            <i>
              🌿 Fresh Ingredients – Handpicked, locally sourced, and free from
              artificial preservatives.<br></br>
              🍽️ Authentic Recipes – Traditional flavors made just like home.
              <br></br>
              🚀 Fast & Reliable Delivery – Hot and fresh, straight from the
              kitchen to your plate.
            </i>
          </p>
        </div>

        <div className="about-iframe-container">
          {/* Left arrow (if needed) */}
          <button className="arrow-btn left-arrow" onClick={prevVideo}>
            &#8672;
          </button>

          <div className="about-iframe-wrapper">
            <div className="about-iframe">
              <iframe
                src={videos[currentVideo]}
                title="About Us Video"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </div>

            <div className="video-indicators">
              {videos.map((_, index) => (
                <span
                  key={index}
                  className={`indicator ${
                    index === currentVideo ? "active" : ""
                  }`}
                  onClick={() => setCurrentVideo(index)}
                ></span>
              ))}
            </div>
          </div>

          {/* Right arrow (if needed) */}
          <button className="arrow-btn right-arrow" onClick={nextVideo}>
            &#8674;
          </button>
        </div>
      </div>

      {/* Floating Images */}
      <img src={floatingImg3} alt="Float 3" className="floating-img img-3" />
      <img src={floatingImg7} alt="Float 4" className="floating-img img-4" />
      <img src={floatingImg5} alt="Float 5" className="floating-img img-5" />
    </section>
  );
};

export default AboutUs;
