import React,{useState} from "react";

export default function BillingRender(props) {
    const billing_URL = "https://rsoi-online-store-billing.herokuapp.com/";

    const orders_URL = "https://rsoi-online-store-orders.herokuapp.com/";
    const suffix = "orders_short/";

    const create_new_orderURL = "https://rsoi-online-store-customers.herokuapp.com/create_new_order/";

    const orderUuid = localStorage.getItem("userCartUUID");

    const [address, setAddress] = useState("");
    const [billtype, setBilltype] = useState("Cash");
    const [phone, setPhone] = useState("");

    function sendBilling(address, billtype, phone) {
        let billingUuid = 0;
        let billingData = {
            payment_method: billtype,
            address: address,
            telephone_number: phone
        };
        let billingJson = JSON.stringify(billingData);
        let smth = {
            isClosed: true
        };
        let smthJson = JSON.stringify(smth);

        fetch(orders_URL + suffix + orderUuid +"/", {
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("access")
                },
            })
            .then(res => res.json())
            .then(
                (result) => {
                    billingUuid = result.billing;
                    console.log(billingUuid);
                })
            .then (
                (error) => {
                    console.log(error);
                })
            .then( () => {
                fetch(billing_URL + billingUuid + "/", {
                    headers: {
                        "Authorization": "Bearer " + localStorage.getItem("access"),
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        },
                    method: "PATCH",
                    body: billingJson
                })
                    .then(res => res.json())
                    .then(
                        (result) => {
                            console.log(result);
                        })
                    .then (
                        (error) => {
                            console.log(error);
                        })
                    .then(() => {
                        fetch(orders_URL + orderUuid + "/", {
                            headers: {
                                "Authorization": "Bearer " + localStorage.getItem("access"),
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                                },
                            method: "PATCH",
                            body: smthJson
                        })
                            .then(res => res.json())
                            .then(
                                (result) => {
                                    console.log(result);
                                }
                            )
                    })
                    .then(() => {
                        fetch(create_new_orderURL + localStorage.getItem("userId") + "/", {
                            headers: {
                                "Authorization": "Bearer " + localStorage.getItem("access")
                            },
                            })
                            .then(res => res.json())
                            .then(
                                (result) => {
                                    console.log(result);
                                    localStorage.setItem("userCartUUID", result.uuid)
                                }
                            )
                    })
            })

        /*fetch(URL + localStorage.getItem("userCartUUID") + "/", {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "PATCH",
            body: data
        }).then(r => console.log("item deleted"))*/
    }

    return (
        <form className="billing_form">
            <div className="login_group">
                <label htmlFor="address" className="login_label">Адрес доставки:</label>
                <input type="text" id="address" className="reg_input" name="address" onChange={e => setAddress(e.target.value)}/>
            </div>
            <div className="login_group">
                <label htmlFor="billtype" className="login_label">Метод оплаты</label>
                <select name="billtype" onChange={e => setBilltype(e.target.value)}>
                    <option value="Cash">Оплата наличными</option>
                    <option value="Card">Оплата картой</option>
                </select>
            </div>
            <div className="login_group">
                <label htmlFor="phone" className="login_label">Телефонный номер:</label>
                <input type="text" id="phone" className="reg_input" name="phone" onChange={e => setPhone(e.target.value)}/>
            </div>
            <button type="button" onClick={() => sendBilling(address, billtype, phone)}>Подтвердить заказ</button>
        </form>
    )
}