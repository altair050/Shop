import React, {useState} from "react";

export default function LoginFormRender({loginCallback}) {

    const URL = "https://rsoi-online-store-auth.herokuapp.com/api/api-token-auth/";
    const user_URL = "https://rsoi-online-store-auth.herokuapp.com/user_info/";
    const customer_URL = "https://rsoi-online-store-customers.herokuapp.com/all_customers/";
    const [logLog, setLogLog] = useState("");
    const [logPass, setLogPass] = useState("");

    function sendLogData(log, pass) {
        let data = {
            username: log,
            password: pass
        };
        let json = JSON.stringify(data);
        // Запрос токенов
        fetch(URL, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: json
        })
            .then(res => res.json())
            .then(
                (result) => {
                    localStorage.setItem("access", result.access);
                    localStorage.setItem("refresh", result.refresh);
                },
                (error) => {
                    console.log("ошибка запрос токенов");
                    console.log(error);
                })
            .then( () => {
                // Запрос userId посетителя
                fetch(user_URL, {
                    headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access")
                    },
                })
                    .then(res => res.json())
                    .then(
                        (result) => {
                            localStorage.setItem("userId" , result.id);
                        }
                    )
                    .then( () => {
                        // Запрос uuid пустой корзины корзины
                        fetch(customer_URL + localStorage.getItem("userId") +"/", {
                            headers: {
                                "Authorization": "Bearer " + localStorage.getItem("access")
                                },
                            })
                            .then(res => res.json())
                            .then(
                                (result) => {
                                    for (let i = 0; i < result.orders.length; i++) {
                                        if (result.orders[i].isClosed === false) {
                                            localStorage.setItem("userCartUUID", result.orders[i].uuid);
                                            break
                                        }
                                    }
                                    //Смена компонента
                                    loginCallback();
                                    },
                                (error) => {
                                    console.log("ошибка запрос пустой корзины");
                                    console.log(error);
                                    }
                                )
                    })
            })
    }

    return (
        <form>
            <div className="login_group">
                <label htmlFor="login" className="login_label">Логин:</label>
                <input type="text" id="login" className="reg_input" value={logLog} onChange={e => setLogLog(e.target.value)}/>
            </div>
            <div className="login_group">
                <label htmlFor="password" className="login_label">Пароль:</label>
                <input type="text" id="password" className="reg_input" name="password" value={logPass} onChange={e => setLogPass(e.target.value)}/>
            </div>
            <button type="button" id="login_button" onClick={() => sendLogData(logLog, logPass)}>Войти</button>
        </form>
    )
}