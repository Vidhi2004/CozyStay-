$(document).ready(function() {
    fetchGuests();
});

function fetchGuests() {
    $.ajax({
        url: '/guest',
        method: 'GET',
        success: function(data) {
            displayGuests(data);
        },
        error: function(error) {
            console.error('Error fetching guests:', error);
        }
    });
}

function displayGuests(guests) {
    const guestList = $('#guest-list');
    guestList.empty();

    if (guests.length > 0) {
        const table = $('<table></table>').addClass('guest-table');
        const headerRow = $('<tr></tr>');
        headerRow.append('<th>ID</th>');
        headerRow.append('<th>Name</th>');
        headerRow.append('<th>Age</th>');
        table.append(headerRow);

        guests.forEach(guest => {
            const row = $('<tr></tr>');
            row.append(`<td>${guest.id}</td>`);
            row.append(`<td>${guest.name}</td>`);
            row.append(`<td>${guest.age}</td>`);
            table.append(row);
        });

        guestList.append(table);
    } else {
        guestList.append('<p>No guests found</p>');
    }
}
