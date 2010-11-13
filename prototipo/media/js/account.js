$(function() {
    $('#course_instance_selection').change(function(event) {
        window.location = event.currentTarget.value
    })
    
    $('#id_delivery_start_date').datetimepicker({})
    $('#id_delivery_end_date').datetimepicker({})
    $('#id_feedback_return_date').datetimepicker({})
})
