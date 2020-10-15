import React from "react";

export default function ChangeAccInfoRender(props) {
    return (
        <div className="login_container">
            <h2 className="login_title">Изменение данных о вас</h2>
            <div className="login_group">
                <label htmlFor="name_change" className="login_label">Новое Имя / Фамилия:</label>
                <input type="text" id="name_change" className="reg_input" name="name_change"/>
            </div>
            <div className="login_group">
                <label htmlFor="password_change" className="login_label">Новый вароль:</label>
                <input type="text" id="password_change" className="reg_input" name="password_change"/>
            </div>
            <div className="login_group">
                <label htmlFor="password_change_again" className="login_label">Повторите новый пароль:</label>
                <input type="text" id="password_change_again" className="reg_input" name="password_change_again"/>
            </div>
            <div className="login_group">
                <label htmlFor="password_old" className="login_label">Старый пароль:</label>
                <input type="text" id="password_old" className="reg_input" name="password_old"/>
            </div>
            <button id="change_change_button">Изменить данные</button>
        </div>
    );
}