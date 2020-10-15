import React from "react";

export default function AccMyBagRender({setAccMenu}) {
    return (
        <ul className="acc_ul">
            <li className="acc_li" onClick={() => setAccMenu("bag")}>
                <span className="a">Корзина</span>
            </li>
            <div className="line"></div>
            <li className="acc_li" onClick={() => setAccMenu("history")}>
                <span className="a">История заказов</span>
            </li>
            <div className="line"></div>
            <li className="acc_li" onClick={() => setAccMenu("settings")}>
                <span className="a">Настройки аккаунта</span>
            </li>
        </ul>
    );
}