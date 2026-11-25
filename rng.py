while (true) {
    const choice = prompt("\n1 - Случайное число\n2 - Выход\nВыберите:");

    if (choice === "1") {
        const rand = Math.floor(Math.random() * 100) + 1;
        alert("\nВыпало: " + rand);
    } else if (choice === "2") {
        alert("\nВыход...");
        break;
    } else {
        alert("\nНеверный выбор");
    }
}