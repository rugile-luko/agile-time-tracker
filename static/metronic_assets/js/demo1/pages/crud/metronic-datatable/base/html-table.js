"use strict";
// Class definition

var KTDatatableHtmlTableDemo = function () {
    // Private functions

    // demo initializer
    var demo = function () {

        var datatable = $('.my-table').KTDatatable({
            // data: {
            // 	saveState: {cookie: false},
            // },
            search: {
                input: $('#generalSearch'),
            },
            columns: [
                {
                    field: "RecordID", title: "#", sortable: !1, width: 20, type: "number", selector: {class: "kt-checkbox--solid"}, textAlign: "center",
                    autoHide: false,
                },
                {
                    field: 'Image',
                    title: 'Image',
                    autoHide: false,
                    width: 40,
                    sortable: !1,
                },
                {
                    field: 'Product',
                    title: 'Product',
                    autoHide: false,
                },
                {
                    field: 'Colors',
                    title: 'Colors',
                    autoHide: false,
                    template: function (row) {
                        const colors_str = row['Colors'];
                        const colors_array = colors_str.split(",");
                        console.log(colors_array);

                        let display_str = '';

                        for (const color_item of colors_array) {
                            let border = "";
                            if (color_item.toLowerCase() === "#ffffff") {
                                border = 'border: 0.5px solid #000000 !important;'
                            }

                            display_str += '<span class="kt-badge kt-badge--outline-2x" style="background-color:' + color_item + ';' + border + '"> </span>'
                        }


                        return display_str
                        // return '<span class="kt-badge ' + status[row['Shopify Sync']].class + ' kt-badge--inline kt-badge--pill">' + row['Shopify Sync'] + '</span>';
                    }
                },
                {
                    field: 'Created',
                    title: 'Created',
                    autoHide: false,
                },
                {
                    field: 'Base Price',
                    title: 'Base Price',
                    autoHide: false,
                },
                {
                    field: 'Your Price',
                    title: 'Your Price',
                    autoHide: false,
                },
                {
                    field: 'Actions',
                    title: 'Actions',
                    autoHide: false,
                },
                {
                    field: 'Shopify Sync',
                    title: 'Shopify Sync',
                    autoHide: true,
                    // callback function support for column rendering
                    template: function (row) {
                        var status = {
                            'Not Imported': {'title': 'Delivered', 'class': ' kt-badge--danger'},
                            'Imported': {'title': 'Success', 'class': ' kt-badge--success'},
                        };
                        return '<span class="kt-badge ' + status[row['Shopify Sync']].class + ' kt-badge--inline kt-badge--pill">' + row['Shopify Sync'] + '</span>';
                    }
                }
                // {
                //     field: "Shopify Sync", width: 1000
                // },
                // {
                //     field: 'Shopify Sync',
                //     type: 'text',
                // },
                // {
                // 	field: 'DepositPaid',
                // 	type: 'number',
                // },
                // {
                // 	field: 'OrderDate',
                // 	type: 'date',
                // 	format: 'YYYY-MM-DD',
                // }, {
                // 	field: 'Status',
                // 	title: 'Status',
                // 	autoHide: false,
                // 	// callback function support for column rendering
                // 	template: function(row) {
                // 		var status = {
                // 			1: {'title': 'Pending', 'class': 'kt-badge--brand'},
                // 			2: {'title': 'Delivered', 'class': ' kt-badge--danger'},
                // 			3: {'title': 'Canceled', 'class': ' kt-badge--primary'},
                // 			4: {'title': 'Success', 'class': ' kt-badge--success'},
                // 			5: {'title': 'Info', 'class': ' kt-badge--info'},
                // 			6: {'title': 'Danger', 'class': ' kt-badge--danger'},
                // 			7: {'title': 'Warning', 'class': ' kt-badge--warning'},
                // 		};
                // 		return '<span class="kt-badge ' + status[row.Status].class + ' kt-badge--inline kt-badge--pill">' + status[row.Status].title + '</span>';
                // 	},
                // }
            ],
        });

        $('#kt_form_status').on('change', function () {
            datatable.search($(this).val().toLowerCase(), 'Status');
        });

        $('#kt_form_type').on('change', function () {
            datatable.search($(this).val().toLowerCase(), 'Type');
        });

        $('#kt_form_status,#kt_form_type').selectpicker();

    };

    return {
        // Public functions
        init: function () {
            // init dmeo
            demo();
        },
    };
}();

jQuery(document).ready(function () {
    KTDatatableHtmlTableDemo.init();
});