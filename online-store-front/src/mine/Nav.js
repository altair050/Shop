import React from "react";
import logo from "./img/logo.png";
import LoginControlRender from "../mine/LoginControl"

export default function NavRender({bagCallback}) {

    return (
        <div className="navbar_bg">
            <div className="container">
                <div className="navbar">
                    <div className="logo">
                        <a href="index.html">
                            <img alt="logo" id="logo_img" src={logo} />
                        </a>
                    </div>
                    <LoginControlRender bagCallback={bagCallback}/>
                </div>
            </div>
        </div>
    );
}