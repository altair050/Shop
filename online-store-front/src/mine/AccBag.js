import React from "react";
export default function AccBagRender(props) {
    return (
        <div className="bag_wrap">
            <h2 className="bag_title">Ваша корзина</h2>
            <div className="bag_title_row">
                <div className="bag_title_count bag_row_item">Количество</div>
                <div className="bag_row_item"> </div>
                <div className="bag_row_item_big"> </div>
                <div className="bag_row_item"> </div>
                <div className="bag_title_price bag_row_item">Цена</div>
            </div>
        </div>
    );
}