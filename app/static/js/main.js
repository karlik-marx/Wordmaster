// Обновляет выбранный алгоритм при клике на карточку с алгоритмом (элементы с атрибутом data-algorithm)
document.querySelectorAll('[data-algorithm]').forEach(i => {
    i.addEventListener('click', () => {
        document.getElementById('selectedAlgorithm').value = i.getAttribute('data-algorithm');
        document.getElementById('selectedAlgorithmName').innerText = i.getAttribute('data-algorithm-name');
    })
})

// Функция для подсчета количества слов и символов в тексте
function updateWordAndCharCount(text) {
    const words = text.trim().match(/[\p{L}\p{M}]+/gu);
    const wordCount = words ? words.length : 0;
    const charCount = text.length;
    document.getElementById('wordCount').textContent = wordCount;
    document.getElementById('charCount').textContent = charCount;
}

// Обновляет содержимое текстового поля (textarea) при выборе файла
document.getElementById('fileInput').addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        document.getElementById('fileName').textContent = file.name;
        const reader = new FileReader();
        reader.onload = function (e) {
            const text = e.target.result;
            document.getElementById('textArea').value = text;
            updateWordAndCharCount(text);
        };
        reader.readAsText(file);
    }
});

// Обновляет количество слов и символов при вводе текста в текстовое поле
document.getElementById('textArea').addEventListener('input', function() {
    const text = this.value;
    updateWordAndCharCount(text);
});




