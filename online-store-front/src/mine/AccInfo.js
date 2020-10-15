import React from "react";


export default function AccInfoRender(props) {
    const infoItem = props.setItem;
        return (
            <div className="accinfo_wrap">
                <h2 className="accinfo_title">Информация о вас</h2>
                <div className="accinfo_title_row">
                    <div className="accinfo_title_name accinfo_row_item">Ваше Имя / Фамилия</div>
                    <div className="accinfo_title_login accinfo_row_item">Ваш логин</div>
                </div>
                <div className="accinfo_item">
                    <div id="accinfo_item_name" className="accinfo_row_item">{infoItem.name}</div>
                    <div id="accinfo_item_login" className="accinfo_row_item">{infoItem.username}</div>
                    <button onClick={() => localStorage.clear()}>выйти</button>
                </div>
            </div>
        );
}