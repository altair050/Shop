import React, {useEffect, useState} from "react";
import AccHeader from "./AccHeader";
import AccBagRender from "./AccBag";
import AccHistoryRender from "./AccHistory";
import AccInfoRender from "./AccInfo";
import AccHistoryItemRender from "./AccHistoryItem";
import AccBagItemRender from "./AccBagItem";
import AccBagSummRender from "./AccBagSumm";
import BillingRender from "./Billing";
import AccBagItemEmptyRender from "./AccBagItemEmpty";
import AccHistoryItemEmptyRender from "./AccHistoryItemEmpty";

export default function AccControlRender() {
    const URL = "https://rsoi-online-store-orders.herokuapp.com/";
    const orderUuid = localStorage.getItem("userCartUUID") + "/";
    const orders_URL = "https://rsoi-online-store-customers.herokuapp.com/all_customers/";
    const [items, setItems] = useState([]);
    const [hisItems, setHisItems] = useState([]);
    const [infoItem, setInfoItem] = useState([]);
    let summ = 0;
    const [menu, setMenu] = useState("bag");

    function foo(bar) {
        setMenu(bar);
    }


    useEffect(() => {
        // Запрос товаров в корзине
        fetch(URL + orderUuid, {
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("access")
                },
            })
            .then(res => res.json())
            .then(
                (result) => {
                    console.log("товары в заказе");
                    console.log(result);
                    setItems(result.itemsInOrder);
                })
            .then (() => {
                fetch(orders_URL + localStorage.getItem("userId") + "/", {
                    headers: {
                        "Authorization": "Bearer " + localStorage.getItem("access")
                    },
                    })
                    .then(res => res.json())
                    .then(
                        (result) => {
                            let closedOrders = [];
                            console.log(result);
                            for (let i = 0; i <result.orders.length; i++) {
                                if (result.orders[i].isClosed === true) {
                                    closedOrders.push(result.orders[i]);
                                }
                            }
                            setInfoItem(result);
                            setHisItems(closedOrders);
                        })
            })
    }, [])

    if (menu === "bag") {
        if (items === null || items.length === 0) {
            return (
                <div>
                    <AccHeader setAccMenu={foo}/>
                    <AccBagItemEmptyRender/>
                </div>
            );
        } else {
            return (
                <div>
                    <AccHeader setAccMenu={foo}/>
                    <AccBagRender/>
                    {
                        items.map((item, index) => {
                            summ += item.price;
                            return <AccBagItemRender key={index} setItem={item}/>;
                        })
                    }
                    <AccBagSummRender props={summ}/>
                    <h2 className="login_title">Оформление заказа</h2>
                    <BillingRender/>
                </div>
            );
        }

    } else if (menu === "history") {
        if (hisItems === null || hisItems.length === 0) {
            return (
                <div>
                    <AccHeader setAccMenu={foo}/>
                    <AccHistoryItemEmptyRender/>
                </div>
            );
        } else {
            return (
                <div>
                    <AccHeader setAccMenu={foo}/>
                    <AccHistoryRender/>
                    {
                        hisItems.map((item, index) => {
                            return <AccHistoryItemRender key={index} setItem={item}/>;
                        })
                    }
                </div>
            );
        }
    } else if (menu === "settings") {
        return (
            <div>
                <AccHeader setAccMenu={foo}/>
                <AccInfoRender setItem={infoItem}/>
            </div>
        );
    }
}