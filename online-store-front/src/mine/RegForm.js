import React, {useState} from "react";

export default function RegFormRender({loginCallback}) {
    const URL = "https://rsoi-online-store-customers.herokuapp.com/register/";
    const create_new_orderURL = "https://rsoi-online-store-customers.herokuapp.com/create_new_order/";
    const [regName, setRegName] = useState("");
    const [regLog, setRegLog] = useState("");
    const [regPass, setRegPass] = useState("");
    let cartcheck = 0;

    function sendRegData(name, log, pass) {
        // Проверка если поля пустые
        if ((name.length === 0) || (log.length === 0) || (pass.length === 0)) {
            alert("заполните красные поля");
        } else {
            // Объект для формирования пост запросы
            let data = {
                username: log,
                name: name,
                password: pass
            };
            // Этот объект переводится в JSON
            let json = JSON.stringify(data);
            // Отправляю данные, чтобы получить токены и userId
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
                        localStorage.setItem("access", result.token.access);
                        localStorage.setItem("refresh", result.token.refresh);
                        localStorage.setItem("userId", result.user.id);
                        cartcheck = result.customer.orders;
                        console.log(result);
                    },
                    (error) => {
                        console.log(error);
                    })
                .then(() => {
                    // Если пустой корзины нет, то запрос на создание новой
                    if (cartcheck === null) {
                        fetch(create_new_orderURL + localStorage.getItem("userId") + "/", {
                            headers: {
                                "Authorization": "Bearer " + localStorage.getItem("access")
                            },
                        })
                            .then(res => res.json())
                            .then(
                                (result) => {
                                    localStorage.setItem("userCartUUID", result.uuid);
                                    loginCallback();
                                }
                            )
                    }
                })
        }
    }
    return (
        <form>
            <div className="login_group">
                <label htmlFor="name_reg" className="login_label">Ваше Имя / Фамилия:</label>
                <input type="text" id="name_reg" className={`reg_input ${regName === ""? "reg_input_wrong": ""}`} name="name_reg" value={regName} onChange={e => setRegName(e.target.value)}/>
            </div>
            <div className="login_group">
                <label htmlFor="login_reg" className="login_label">Логин:</label>
                <input type="text" id="login_reg" className={`reg_input ${regLog === ""? "reg_input_wrong": ""}`}name="login_reg" value={regLog} onChange={e => setRegLog(e.target.value)}/>
            </div>
            <div className="login_group">
                <label htmlFor="password_reg" className="login_label">Пароль:</label>
                <input type="text" id="password_reg" className={`reg_input ${regPass === ""? "reg_input_wrong": ""}`} name="password_reg" value={regPass} onChange={e => setRegPass(e.target.value)}/>
            </div>
            <button type="button" id="reg_button" onClick={() => sendRegData(regName, regLog, regPass)}>Зарегистрироваться</button>
        </form>
    )
}