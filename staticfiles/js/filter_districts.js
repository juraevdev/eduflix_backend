(function($) {
    $(document).ready(function() {
        var regionField = $("#id_region");
        var districtField = $("#id_district");
        var districtsData = JSON.parse(districtField.attr("data-districts").replace(/'/g, '"'));

        function updateDistricts() {
            var selectedRegion = regionField.val();
            var districts = districtsData[selectedRegion] || [];
            
            districtField.empty();
            $.each(districts, function(index, district) {
                districtField.append(new Option(district, district));
            });
        }

        regionField.change(updateDistricts);
        updateDistricts();
    });
})(django.jQuery);
