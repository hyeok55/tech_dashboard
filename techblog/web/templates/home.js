document.addEventListener("DOMContentLoaded", function () {
    //검색 이벤트 처리
    const searchBox = document.getElementById("search-box");
    const searchIcon = document.getElementById("search-icon");

    searchBox.addEventListener("focus", function () {
        searchBox.setAttribute("placeholder", "");
    });

    searchBox.addEventListener("blur", function () {
        if (searchBox.value === "") {
            searchBox.setAttribute("placeholder", "Search");
        }
    });


    //대시보드 이벤트 처리
    const allButton = document.getElementById("all-button");
    const companyButton = document.getElementById("company-button");
    const chartContainer = document.getElementById("chart-container");

    // 전체 버튼을 클릭했을 때의 처리
    allButton.addEventListener("click", function () {
        // PyChart를 사용하여 그래프를 그리는 코드를 추가
        chartContainer.innerHTML = "<p>전체 그래프를 표시</p>";
    });

    // 기업별 버튼을 클릭했을 때의 처리
    companyButton.addEventListener("click", function () {
        chartContainer.innerHTML = `
            <div class="company-list">
                <button id="sokka-button">쏘카</button>
                <button id="naver-button">네이버</button>
            </div>
        `;
        console.log("print hi");
    });
    // 특정정기업 버튼 클릭했을시 처리
    chartContainer.addEventListener("click", function (event) {
        if (event.target.id === "sokka-button") {
            // PyChart를 사용하여 쏘카 그래프를 그리는 코드를 추가
            chartContainer.innerHTML = "<p>쏘카 그래프를 표시</p>";
        } else if (event.target.id === "naver-button") {
            // PyChart를 사용하여 네이버 그래프를 그리는 코드를 추가
            chartContainer.innerHTML = "<p>네이버 그래프를 표시</p>";
        }
    });
});
