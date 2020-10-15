import React from 'react';

export default function ProductRender(props) {
    const URL = "https://rsoi-online-store-orders.herokuapp.com/";
    const suffix = "orders_short/";
    const orderUuid = localStorage.getItem("userCartUUID") + "/";

    const productItem = props.setItem;


    function buttonPatch(itemUuid) {
        let data = [];

        if (localStorage.getItem("userCartUUID")) {
            fetch(URL + suffix + orderUuid, {
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access")
                    },
                })
                .then(res => res.json())
                .then(
                    (result) => {
                        console.log(result);
                        if (result.itemsInOrder === null) {
                            result.itemsInOrder = [];
                        }
                        result.itemsInOrder.push(itemUuid);
                        data = JSON.stringify(result);
                    },
                    (error) => {
                        console.log("Ошибка на Гет товара");
                        console.log(error);
                    }
                )
                .then( () => {
                        fetch(URL + orderUuid, {
                            headers: {
                                "Authorization": "Bearer " + localStorage.getItem("access"),
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                            },
                            method: "PATCH",
                            body: data
                        }).then(r => console.log("item added"))
                    }
                );
        } else {
            alert("YOU NEED TO REGISTER OR LOGIN TO USE CART ADDITING");
        }

    }
    return (
        <div className="product" id={productItem.uuid}>
            <img className="product_img" alt={productItem.brand + " " + productItem.name} src={productItem.image}/>
            <div className="product_info">
                <div className="product_name">{productItem.brand}&nbsp;{productItem.name}</div>
                <div className="product_price">
                    от&nbsp;{productItem.price}
                    <span className="price"></span>
                    <span className="rouble">&nbsp;Р&nbsp;Цвет:&nbsp;{productItem.color}</span>
                </div>
                <button className="product_button" onClick={() => buttonPatch(productItem.uuid)}>В корзину</button>
            </div>
        </div>
    );
}