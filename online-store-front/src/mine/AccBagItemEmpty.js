import React from "react";

export default function AccBagItemEmptyRender (props) {
    return (
        <div className="bag_item_row">
            <div className="bag_item_info bag_row_item_big">
                <span className="bag_item_name">Нет товаров в корзине</span>
            </div>
        </div>
    );
}