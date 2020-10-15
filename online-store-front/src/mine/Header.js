import React from "react";

export default function HeaderRender({appCallback}) {
    return (
        <div className="menu">
            <div className="container">
                <ul className="menu_ul">
                    <li className="menu_li" onClick={() => appCallback("Tshirt", true)}>
                        <span className="a">футболки</span>
                    </li>
                    <li className="menu_li" onClick={() => appCallback("Headwear", true)}>
                        <span className="a">головные уборы</span>
                    </li>
                    <li className="menu_li" onClick={() => appCallback("Jacket", true)}>
                        <span className="a">куртки</span>
                    </li>
                    <li className="menu_li" onClick={() => appCallback("Hoodie", true)}>
                        <span className="a">толстовки</span>
                    </li>
                    <li className="menu_li" onClick={() => appCallback("Pants", true)}>
                        <span className="a">штаны</span>
                    </li>
                    <li className="menu_li" onClick={() => appCallback("Footwear", true) }>
                        <span className="a">обувь</span>
                    </li>
                </ul>
            </div>
        </div>
    );
}