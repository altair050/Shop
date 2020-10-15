import React from "react";

export default function AccBagSummRender({props}) {
    return (
        <div className="bag_summary_wrap">
            <div className="summary_title">Итого:</div>
            <div id="summary_number">{props}</div>
        </div>
    );
}