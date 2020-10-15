import React from 'react';

export default function LoginControlRender({bagCallback}) {

    if (localStorage.getItem("access")) {
        return (
            <div className="navbar_acc" onClick={()=> bagCallback()}>
                <span className="a"> корзина/мой аккаунт</span>
            </div>
        )
    } else {
        return (
            <div className="navbar_acc" onClick={()=>bagCallback()}>
                <span className="a">вход/регистрация</span>
            </div>
        )
    }
}
