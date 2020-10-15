import React, {useState} from "react";
import AccControlRender from "./AccControl";
import RegFormRender from "./RegForm";
import LoginFormRender from "./LoginForm";

export default function LoginRender(props) {
    const [isLoginPage, setLoginPage] = useState(true);
    const [isLoggedIn, setLoggedIn] = useState(false);

    function logged() {
        setLoggedIn(true);
    }
    if (localStorage.getItem("access")){
        return (
            <AccControlRender/>
        );
    } else {
        if (isLoginPage) {
            return (
                <div className="login_container">
                    <h2 className="login_title">Вход</h2>
                    <LoginFormRender loginCallback={logged}/>
                    <span>или <span className="a" onClick={() => setLoginPage(false)}>регистрация</span></span>
                </div>
            );
        } else {
            return (
                <div className="login_container">
                    <h2 className="login_title">Регистрация</h2>
                    <RegFormRender loginCallback={logged}/>
                    <span>или <span className="a" onClick={() => setLoginPage(true)}>войти</span></span>
                </div>
            );
        }
    }
}