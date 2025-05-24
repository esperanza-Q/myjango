document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.querySelector('.addIngredient');
    const nameInput = document.getElementById('ingredient-name');
    const amountInput = document.getElementById('ingredient-amount');
    const unitSelect = document.getElementById('ingredient-unit');
    const ul = document.getElementById('ingredients-ul');
    const hiddenInputsDiv = document.getElementById('ingredients-hidden-inputs');

    if (addBtn) {
        addBtn.addEventListener('click', function () {
            const name = nameInput.value.trim();
            const amount = amountInput.value.trim();
            const unit = unitSelect.value;

            if (!name || !amount) {
                alert('재료 이름과 양을 입력해주세요!');
                return;
            }

            // 리스트에 추가
            const li = document.createElement('li');
            li.textContent = `${name} - ${amount} ${unit}`;
            ul.appendChild(li);

            // 숨은 input 추가 (서버 전송용)
            const inputName = document.createElement('input');
            inputName.type = 'hidden';
            inputName.name = 'ingredients_name[]';
            inputName.value = name;

            const inputAmount = document.createElement('input');
            inputAmount.type = 'hidden';
            inputAmount.name = 'ingredients_amount[]';
            inputAmount.value = amount;

            const inputUnit = document.createElement('input');
            inputUnit.type = 'hidden';
            inputUnit.name = 'ingredients_unit[]';
            inputUnit.value = unit;

            hiddenInputsDiv.appendChild(inputName);
            hiddenInputsDiv.appendChild(inputAmount);
            hiddenInputsDiv.appendChild(inputUnit);

            // 입력칸 초기화
            nameInput.value = '';
            amountInput.value = '';
            unitSelect.selectedIndex = 0;
        });
    }
});
