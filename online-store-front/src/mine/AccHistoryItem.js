import React from "react";

export default function AccHistoryItemRender(props) {

    const historyItem = props.setItem;

        return (
            <div className="history_item_row">
                <div className="history_item_info history_row_item">
                    <div className="history_item_info_line">
                        {
                            historyItem.itemsInOrder.map((item, index) => {return <div id="history_item_info_line_name" key={index}>{item.name} 1шт</div>})
                        }
                    </div>
                </div>
                <div className="history_row_item">{historyItem.billing.payment_method}</div>
                <div className="history_row_item">{historyItem.billing.address + ". Телефон: " + historyItem.billing.telephone_number}</div>
            </div>
        );
}