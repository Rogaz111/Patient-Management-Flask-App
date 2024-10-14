// Functionality for "Select All" checkbox -- view_appointment.html --
document.getElementById('selectAll').addEventListener('click', function() {
console.log('Select All button clicked')
var checkboxes = document.querySelectorAll('.appointment-checkbox');
checkboxes.forEach(function(checkbox) {
  checkbox.checked = document.getElementById('selectAll').checked;
    });
});

// Capture changes in the contenteditable fields for date and time
document.querySelectorAll('td[contenteditable="true"]').forEach(function (cell) {
    cell.addEventListener('blur', function () {
        var newValue = this.textContent;  // The updated value
        var appointmentId = this.closest('tr').querySelector('.appointment-checkbox').value;  // Get the appointment ID
        var fieldName = this.cellIndex === 5 ? 'appointment_date' : 'appointment_time'; // Identify if it's date or time

        // Make an AJAX call to update the appointment in the backend
        fetch('/update_appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                appointment_id: appointmentId,
                field: fieldName,
                new_value: newValue
            })
        }).then(response => {
            if (response.ok) {
                console.log('Update successful');
                console.log(appointmentId.toString() + ' ' + fieldName.toString() + ' ' + newValue.toString());
            } else {
                console.error('Update failed');
            }
        });
    });
  });