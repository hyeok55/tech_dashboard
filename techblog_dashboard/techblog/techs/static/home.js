document.addEventListener("DOMContentLoaded", function () {
    //검색 submit 이벤트
    document.getElementById('search-icon').addEventListener('click', function () {
        var inputElement = document.querySelector('input[name="user_input"]');
        var inputValue = inputElement.value;
        var form = document.getElementById('searchForm');
        form.action = '/techs/search/' + inputValue;
        console.log(inputValue);
        form.submit();
    });

    //대시보드 이벤트 처리
    const allButton = document.getElementById("all-button");
    const companyButton = document.getElementById("company-button");
    const chartContainer = document.getElementById("chart-container");
    // const companyList = document.getElementById("company-list")

    // 전체 버튼을 클릭했을 때의 처리
    allButton.addEventListener("click", function () {
        var img = document.createElement("img");
        img.src="/static/chart/all.png"
        img.style.height="1100px";
        img.style.objectFit="cover";

        chartContainer.innerHTML="";
        chartContainer.appendChild(img);

        // fetch ("visualization_all/")
        //     .then(response => response.json())
        //     .then(data => {
        //         // Plotly.newplot('chart-container', data.plot_div, {});
        //         chartContainer.innerHTML = data.plot_div;
        //     })
        //     .catch(error => console.error('Error: ', error))

        
    });

//     // // 기업별 버튼을 클릭했을 때의 처리
    companyButton.addEventListener("click", function () {
        chartContainer.innerHTML = `
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
        console.log('print hi');

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


// companyList.addEventListener("click", function(event) {
//     const clickedButton = event.target;
//     if(clickedButton.classList.contains("company-buttion")) {
//         const companyName = clickedButton.getAttribute("data-company-name");
//         alert("selected company: ", companyName);
//     }
// });


//     // 특정정기업 버튼 클릭했을시 처리
    chartContainer.addEventListener("click", function (event) {
        if (event.target.id === "gangnam-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/강남언니.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "naver-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/네이버.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "danggn-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/당근.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "devocean-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/데보션.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "line-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/라인.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "musinsa-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/무신사.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "bank-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/뱅크샐러드.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "socar-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/쏘카.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "watcha-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/왓챠.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "yogiyo-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/요기요.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "woowa-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/우아한형제들.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "est-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/이스트소프트.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "kakao-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/카카오.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "kakaoenter-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/카카오엔터프라이즈.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "kakaopay-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/카카오페이.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "coupang-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/쿠팡.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "hc-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/하이퍼커넥트.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        } else if (event.target.id === "skplanet-button") {
            var img = document.createElement("img");
            img.src = '/static/chart/SK플래닛.png';
            img.style.height="1100px";
            img.style.objectFit="cover";

            chartContainer.innerHTML="";
            chartContainer.appendChild(img);
        }
        
    });
});