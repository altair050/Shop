import React, {useState, useEffect} from 'react';
import './mine/css/main.css';
import HeaderRender from "./mine/Header";
import ProductRender from "./mine/Product";
import NavRender from "./mine/Nav";
import LoginRender from "./mine/Login";

function App() {
    const URL = "http://127.0.0.1:8000/";

    const [isMenu, setMenu] = useState(true);
    function loginFunc() {
        setMenu(false);
    }

    const [menuChoice, setChoice] = useState("Lipstick");
    function menuFunc(list, la) {
        setChoice(list);
        setMenu(la);
    }

    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch(URL)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    setItems(result);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                })
    }, [])


    if (isMenu) {
        if (error) {
            return <div>Ошибка: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Загрузка...</div>;
        } else {
            return (
                <div>
                    <header>
                        <NavRender bagCallback={loginFunc}/>
                        <HeaderRender appCallback={menuFunc}/>
                    </header>
                    <main>
                        <div className="container">
                            <div className="product_list">
                                {
                                    items.map(function (item, index) {
                                        if (item.category === menuChoice) {
                                            return (
                                                <ProductRender key={index} setItem={item}/>
                                            );
                                        }
                                    })
                                }
                            </div>
                        </div>
                    </main>
                </div>
            );
        }
    } else {
        return (
            <div>
                <header>
                    <NavRender bagCallback={loginFunc}/>
                    <HeaderRender appCallback={menuFunc}/>
                </header>
                <main>
                    <div className="container">
                        <LoginRender/>
                    </div>
                </main>
            </div>
        );
    }

}

export default App;
