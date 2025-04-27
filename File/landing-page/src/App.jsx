import React, { useState } from "react";
import {Link} from "react-router-dom";
import "./index.css";
import logo from "./images/logo.png";
import landingImg from "./images/bleaf2.png";
import floatingImg1 from "./images/float1.png";
import floatingImg2 from "./images/float2.png";
import floatingImg3 from "./images/float3.png";
import floatingImg4 from "./images/float4.png";
import floatingImg5 from "./images/float5.png";
import floatingImg6 from "./images/float6.png";
import floatingImg7 from "./images/float7.png";
import AboutUs from "./AboutSec";

const App = () => {
  const [activeSection, setActiveSection] = useState(0);

  // Handles scroll and updates active section
  const handleScroll = (e) => {
    const container = e.target;
    const scrollHeight = container.scrollHeight - container.clientHeight;
    const scrollTop = container.scrollTop;
    const sectionHeight = scrollHeight / 4;
    const newActiveSection = Math.min(3, Math.floor(scrollTop / sectionHeight));

    setActiveSection(newActiveSection);
  };

  return (
    <div className="app-container" id="home">
      {/* Logo Section */}
      <div className="logo-section">
        <div className="logo">
          <img src={logo} alt="Logo"></img>
        </div>
      </div>

      {/* Navbar Section */}
      <div className="navbar">
      <a href="#landing" className="nav-link">
        Home
        </a>
        <a href="#about" className="nav-link">
          About Us
        </a>
        <a href="#packages" className="nav-link">
          Packages
        </a>
        <a href="#contact" className="nav-link">
          Contact
        </a>
        <p>
          <Link to="/login">Login/Signup</Link>
        </p>
      </div>

      {/* Scrollable Content */}
      <div className="scroll-container" onScroll={handleScroll}>
        <div className="main-content">
          {/* Landing Section */}
          <section className="section landing-section " id="landing">
            <div className="layer-content">
              <div className="landing-content">
                <h1>
                  Fresh. Homemade.<br></br>
                  <span class="cursive-text">delivered with love.</span>
                </h1>
                <br></br>
                <h3>
                  Craving the warmth of a home-cooked meal but short on time?{" "}
                  <br></br>We bring you authentic, homemade dishes prepared with
                  care, <br></br>
                  just like how <b>mom</b> makes it. From traditional favorites
                  to wholesome, nourishing meals, enjoy food that’s made with
                  fresh ingredients, no shortcuts, and all the love.
                </h3>
                <a href="#packages">
                <button className="btn">Place Order Now!</button>
                </a>
              </div>
              
              <img src={landingImg} alt="landing-img" className="landing-img" />
              <img
                src={floatingImg1}
                alt="Float 1"
                className="floating-img img-1"
              />
              <img
                src={floatingImg2}
                alt="Float 2"
                className="floating-img img-2"
              />
            </div>
          </section>

          <AboutUs />

          <section
            className="section  landing-section packages-section"
            id="packages"
          >
            <div className="layer-content">
              <h2 className="packages-title">Our Packages</h2>
              <div className="packages-container">
                {/* Basic Package */}
                <div className="package-box" id="breakfast">
                  <h3>Breakfast</h3>
                  <p className="package-price">$9.99/month</p>
                  {/*<ul>
                      <li> 5GB Storage</li>
                      <li>Basic Support</li>
                      <li>Limited Features</li>
                      <li> 5GB Storage</li>
                      <li>Basic Support</li>
                      <li>Limited Features</li>
                    </ul>*/}
                  Something delicious is cooking....<br></br>
                  {/*<button className="btn">Choose Package</button>*/}
                </div>
                <div className="package-box " id="lunch">
                  <h3>Lunch</h3>
                  <p className="package-price">$19.99/month</p>
                  <h4>
                    <i>Authentic Homefood Combo</i>
                  </h4>
                  <ul>
                    <li> Rice</li>
                    <li> Sambhar</li>
                    <li> Rasam</li>
                    <li> Kootu</li>
                    <li> Poriyal</li>
                    <li> Buttermilk</li>
                  </ul>
                  <button className="btn">Choose Combo</button>
                  <br></br>
                  <h4>
                    <i>Fusion Combo</i>
                  </h4>
                  <ul>
                    <li> Rice 100gms</li>
                    <li> Chapati</li>
                    <li> Gravy</li>
                    <li> Kootu</li>
                    <li> Poriyal</li>
                    <li> Buttermilk</li>
                  </ul>
                  <button className="btn">Choose Combo</button>
                </div>

                {/* Premium Package */}
                <div className="package-box" id="dinner">
                  <h3>Dinner</h3>
                  <p className="package-price">$29.99/month</p>
                  <ul>
                    <li> Main Dish - Any 2 </li>
                    <li> Side Dish - Any 2 </li>
                  </ul>
                  <button className="btn">Choose Package</button>
                </div>
              </div>
              <img
                src={floatingImg4}
                alt="Float 3"
                className="floating-img img-1"
              />
              <img
                src={floatingImg6}
                alt="Float 4"
                className="floating-img img-3"
              />
            </div>
          </section>

          <section className="section landing-section" id="contact">
            <div className="contact-section">
              <div class="contact-form">
                <h2>Contact Us</h2>
                <p>
                  <center>
                    We’d love to hear from you! Drop us a message or give us a
                    call!
                  </center>
                </p>

                <label for="phone">Phone Number:</label>
                <input
                  type="text"
                  id="phone"
                  placeholder="Enter your phone number"
                ></input>

                <label for="message">Your Message:</label>
                <textarea id="message"></textarea>

                <button type="submit">Send Message</button>
              </div>
              <img
                src={floatingImg3}
                alt="Float 3"
                className="floating-img img-2"
              />
              <img
                src={floatingImg5}
                alt="Float 5"
                className="floating-img img-5"
              />
              <img
                src={floatingImg7}
                alt="Float 4"
                className="floating-img img-4"
              />
            </div>
          </section>
        </div>
      </div>

      {/* Custom Scrollbar */}
      <div className="custom-scrollbar">
        {[0, 1, 2, 3].map((index) => (
          <div
            key={index}
            className={`scroll-stage ${
              activeSection === index ? "active" : ""
            }`}
          ></div>
        ))}
      </div>
    </div>
  );
};

export default App;
