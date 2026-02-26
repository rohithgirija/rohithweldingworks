import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Welding Website", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["Login", "Buttons", "Animated", "Style Sites"])

if page == "Login":
    # Login Page HTML
    login_html = """
    <div style="display:flex;justify-content:center;align-items:center;height:80vh;">
    <div class="login-box">
        <h2>🔥 Login 🔥</h2>
        <form onsubmit="return validateLogin()">
            <div class="input-box">
                <label>Username</label>
                <input type="text" id="username" required>
            </div>
            <div class="input-box">
                <label>Password</label>
                <input type="password" id="password" required>
            </div>
            <button type="submit" class="btn">Login</button>
            <div class="error" id="errorMsg"></div>
        </form>
    </div>
    </div>

    <style>
    body {background: url('https://images.unsplash.com/photo-1595843843649-133b9017ef54?auto=format&fit=crop&w=1470&q=80') no-repeat center center fixed; background-size: cover;}
    .login-box{position:relative;width:350px;padding:40px;border-radius:15px;background:#111;color:white;text-align:center;overflow:hidden;
    box-shadow:0 0 20px red,0 0 40px orange,0 0 60px yellow;animation:pulseGlow 2s infinite alternate;}
    @keyframes pulseGlow{0%{box-shadow:0 0 15px red,0 0 30px orange,0 0 45px yellow;}100%{box-shadow:0 0 25px red,0 0 50px orange,0 0 75px yellow;}}
    .login-box::before{content:"";position:absolute;top:-3px;left:-3px;right:-3px;bottom:-3px;background:linear-gradient(45deg,red,orange,yellow,red,orange,yellow);background-size:400%;z-index:-1;border-radius:20px;animation:fire 3s linear infinite;filter:blur(5px);}
    @keyframes fire{0%{background-position:0% 50%;}100%{background-position:400% 50%;}}
    .input-box input{width:100%;padding:10px;margin-top:5px;border:none;outline:none;border-radius:8px;background:#222;color:white;box-shadow:0 0 10px orange;transition:0.3s;}
    .input-box input:focus{box-shadow:0 0 10px yellow,0 0 20px orange,0 0 30px red;}
    .btn{width:100%;padding:12px;margin-top:20px;border:none;border-radius:8px;background:linear-gradient(45deg,orange,red);color:rgb(224,220,220);font-weight:bold;cursor:pointer;transition:0.3s;box-shadow:0 0 15px orange;}
    .btn:hover{color:white;box-shadow:0 0 20px red,0 0 40px orange,0 0 60px yellow;transform:scale(1.05);}
    .error{color:yellow;margin-top:10px;}
    .login-box::after{content:"";position:absolute;width:200%;height:100%;top:-50%;left:-50%;background:radial-gradient(circle, rgba(255,140,0,0.3), transparent 70%);animation:rotateFire 6s linear infinite;z-index:-2;}
    @keyframes rotateFire{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
    </style>

    <script>
    function validateLogin(){
        var user = document.getElementById("username").value;
        var pass = document.getElementById("password").value;
        if(user==="admin" && pass==="1234"){
            alert("Login Successful!"); return false;
        } else{
            document.getElementById("errorMsg").innerText = "Invalid Username or Password";
            return false;
        }
    }
    </script>
    """
    components.html(login_html, height=700, scrolling=True)

elif page == "Buttons":
    buttons_html = """
    <div style="text-align:center; margin-top:50px;">
        <button style="padding:15px 40px; font-size:18px; margin:10px; background:#d41414; color:white; border:none; border-radius:50px;" onclick="alert('Continue Clicked')">Continue</button>
        <button style="padding:15px 40px; font-size:18px; margin:10px; background:#ff9800; color:white; border:none; border-radius:50px;" onclick="alert('Calculator Open')">Calculator</button>
        <button style="padding:15px 40px; font-size:18px; margin:10px; background:#00bcd4; color:white; border:none; border-radius:10px;" onclick="alert('Click Here Pressed')">Click Here</button>
    </div>
    """
    components.html(buttons_html, height=300)

elif page == "Animated":
    animated_html = """
    <div style="display:flex; padding:20px; font-family:Arial, sans-serif;">
        <div style="width:20%; background:white; padding:15px; border-radius:5px;">
            <h3>Related Category</h3>
            <p>MIG Welding Services</p>
            <p>TIG Welding Services</p>
            <p>Aluminium Welding</p>
        </div>
        <div style="width:55%; margin:0 20px;">
            <div style="background:white;padding:15px;margin-bottom:15px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                <img src="https://via.placeholder.com/120x80" style="float:left;margin-right:15px;">
                <h3>Welding Fabrication Service</h3>
                <p style="color:green;font-weight:bold;">₹ 135 / Kg</p>
                <p>Location: Coimbatore</p>
                <a href="#" style="background:teal;color:white;padding:8px 12px;border-radius:4px;text-decoration:none;">Contact Supplier</a>
                <div style="clear:both;"></div>
            </div>
            <div style="background:white;padding:15px;margin-bottom:15px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.1);">
                <img src="https://via.placeholder.com/120x80" style="float:left;margin-right:15px;">
                <h3>TIG Welding Service</h3>
                <p style="color:green;font-weight:bold;">₹ 530 / Day</p>
                <p>Industrial Usage</p>
                <a href="#" style="background:teal;color:white;padding:8px 12px;border-radius:4px;text-decoration:none;">View Mobile Number</a>
                <div style="clear:both;"></div>
            </div>
        </div>
        <div style="width:25%; background:white;padding:15px;border-radius:5px;">
            <h3>Get Best Sellers</h3>
            <input type="text" placeholder="Enter your mobile" style="width:100%;padding:8px;margin-bottom:10px;">
            <button style="width:100%;padding:10px;background:purple;color:white;border:none;border-radius:4px;">Submit Requirement</button>
        </div>
    </div>
    """
    components.html(animated_html, height=600, scrolling=True)

elif page == "Style Sites":
    style_html = """
    <div style="display:flex; flex-direction:column; align-items:center; margin-top:50px;">
        <div style="background:linear-gradient(45deg,#ff6600,#ff0000);color:white;margin-bottom:15px;padding:18px;border-radius:12px;text-align:center;font-weight:bold;cursor:pointer;" onclick="window.open('https://www.google.com','_blank')">1. Google</div>
        <div style="background:linear-gradient(45deg,#ff6600,#ff0000);color:white;margin-bottom:15px;padding:18px;border-radius:12px;text-align:center;font-weight:bold;cursor:pointer;" onclick="window.open('https://www.flipkart.com','_blank')">2. Flipkart</div>
        <div style="background:linear-gradient(45deg,#ff6600,#ff0000);color:white;margin-bottom:15px;padding:18px;border-radius:12px;text-align:center;font-weight:bold;cursor:pointer;" onclick="window.open('https://www.amazon.in','_blank')">3. Amazon</div>
        <div style="background:linear-gradient(45deg,#ff6600,#ff0000);color:white;margin-bottom:15px;padding:18px;border-radius:12px;text-align:center;font-weight:bold;cursor:pointer;" onclick="window.open('https://www.youtube.com','_blank')">4. YouTube</div>
        <div style="background:linear-gradient(45deg,#ff6600,#ff0000);color:white;margin-bottom:15px;padding:18px;border-radius:12px;text-align:center;font-weight:bold;cursor:pointer;" onclick="window.open('https://www.google.com/chrome/','_blank')">5. Chrome</div>
    </div>
    """
    components.html(style_html, height=600)