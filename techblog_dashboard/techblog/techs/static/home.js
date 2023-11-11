document.addEventListener("DOMContentLoaded", function () {
    //검색 submit 이벤트
    function handleSearch() {
        var inputElement = document.querySelector('input[name="user_input"]');
        var inputValue = inputElement.value;
        var form = document.getElementById('searchForm');
        form.action = '/techs/search/' + inputValue;
        console.log(inputValue);
        form.submit();
    }

    document.getElementById('search-icon').addEventListener('click', handleSearch);

    var inputElement = document.getElementById('search-box');
    inputElement.addEventListener('keydown', function (event) {
        if (event.keyCode === 13) {
            handleSearch();
        }
    });

    const btn1 = document.getElementById("all-button");
    const btn2 = document.getElementById("company-button");

    function allClick() {
        btn1.classList.add("active");
        btn2.classList.remove("active");
    }

    function companyClick() {
        btn1.classList.remove("active");
        btn2.classList.add("active");
    }

    btn1.addEventListener("click", allClick);
    btn2.addEventListener("click", companyClick);


    //대시보드 이벤트 처리
    const allButton = document.getElementById("all-button");
    const companyButton = document.getElementById("company-button");
    const chartContainer = document.getElementById("chart-container");
    const companyList = document.getElementById("company-list");

    // 전체 버튼을 클릭했을 때의 처리
    allButton.addEventListener("click", function () {
        companyList.innerHTML="";
        chartContainer.innerHTML="";
        fetch ("visualization_all/")
            .then(response => response.json())
            .then(data => {
                var fig = JSON.parse(data.plot_div);
                Plotly.newPlot('chart-container', fig.data, fig.layout);
            })
            .catch(error => console.error('Error: ', error))
    });

//     // // 기업별 버튼을 클릭했을 때의 처리
    companyButton.addEventListener("click", function () {
        chartContainer.innerHTML="";
        companyList.innerHTML = `
            <div class="company-list">
                <button id="gangnam-button">강남언니</button>
                <button id="naver-button">네이버</button>
                <button id="danggn-button">당근마켓</button>
                <button id="devocean-button">데보션</button>
                <button id="line-button">라인</button>
                <button id="musinsa-button">무신사</button>
                <button id="bank-button">뱅크샐러드</button>
                <button id="socar-button">쏘카</button>
                <button id="watcha-button">왓챠</button>
                <button id="yogiyo-button">요기요</button>
                <button id="woowa-button">우아한형제들</button>
                <button id="est-button">이스트소프트</button>
                <button id="kakao-button">카카오</button>
                <button id="kakaoenter-button">카카오 엔터프라이즈</button>
                <button id="kakaopay-button">카카오페이</button>
                <button id="coupang-button">쿠팡</button>
                <button id="hc-button">하이퍼커넥트</button>
                <button id="skplanet-button">SK플래닛</button>
            </div>
        `;

        // fetch ("company_list/")
        //     .then(response => response.json)
        //     .then(data => {
        //         const buttonsHTML = data.companies.map(companies => {
        //             return `<button class="company-button" data-company-name="${companies.company_name}">
        //                         ${companies.company_name}
        //                     </button>`;
        //         }).join(" ");

        //         companyList.innerHTML = buttonsHTML;
        //     })
        //     .catch(error => console.error('Error: ', error))
    });


    // 특정기업 버튼 클릭했을시 처리
    companyList.addEventListener("click", function (event) {
        if (event.target.id === "gangnam-button") {
            fetch ("company_chart/강남언니")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "naver-button") {
            fetch ("company_chart/네이버")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "danggn-button") {
            fetch ("company_chart/당근")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "devocean-button") {
            fetch ("company_chart/데보션")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))
            
        } else if (event.target.id === "line-button") {
            fetch ("company_chart/라인")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "musinsa-button") {
            fetch ("company_chart/무신사")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "bank-button") {
            fetch ("company_chart/뱅크샐러드")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "socar-button") {
            fetch ("company_chart/쏘카")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "watcha-button") {
            fetch ("company_chart/왓챠")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "yogiyo-button") {
            fetch ("company_chart/요기요")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "woowa-button") {
            fetch ("company_chart/우아한형제들")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "est-button") {
            fetch ("company_chart/이스트소프트")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "kakao-button") {
            fetch ("company_chart/카카오")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "kakaoenter-button") {
            fetch ("company_chart/카카오엔터프라이즈")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "kakaopay-button") {
            fetch ("company_chart/카카오페이")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "coupang-button") {
            fetch ("company_chart/쿠팡")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "hc-button") {
            fetch ("company_chart/하이퍼커넥트")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))

        } else if (event.target.id === "skplanet-button") {
            fetch ("company_chart/SK플래닛")
                .then(response => response.json())
                .then(data => {
                    var fig = JSON.parse(data.company_div);
                    Plotly.newPlot('chart-container', fig.data, fig.layout);
                })
                .catch(error => console.error('Error: ', error))
        }
        
    });
});