//
// $(document).ready(function() {
//     $('#person_table').DataTable( {
//         "paging":   false,
//         "scrollY": "calc(100vh - 300px)", //75vh
//         "scrollCollapse": true,
//         "info":     false,
//         dom: 'Bfrtip',
//         buttons: [
//             'columnsToggle',
//             {
//                extend: 'colvisGroup',
//                text: 'Mails',
//                show: [ 4 ],
//                hide: [ 0, 1, 2, 3, 5, 6, 7, 8, 9, 10 ]
//            },
//            {
//                 extend: 'colvisGroup',
//                 text: 'Show all',
//                 show: ':hidden'
//             }
//         ]
//
//     } );
// } );
//

///////////////////////////////////////////////////////////////

$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#person_table thead tr').clone(true).appendTo( '#person_table thead' );
    $('#person_table thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="搜尋 '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    var table = $('#person_table').DataTable( {
        orderCellsTop: true,
        fixedHeader: true,
        paging: false,
        scrollY: "calc(100vh - 300px)", //75vh
        scrollCollapse: true,
        info: false,
        dom: 'Brtip', //Bfrtip
        language: { "zeroRecords": "找不到資料" },
        buttons: [
            'columnsToggle',
           {
                extend: 'colvisGroup',
                text: '顯示全部',
                show: ':hidden'
            },
            {
               extend: 'colvisGroup',
               text: '只顯示信箱',
               show: [ 4 ],
               hide: [ 0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11 ]
           }
        ]
    } );
} );



////////// PI
$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#pi_table thead tr').clone(true).appendTo( '#pi_table thead' );
    $('#pi_table thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="搜尋 '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    var table = $('#pi_table').DataTable( {
        orderCellsTop: true,
        fixedHeader: true,
        paging: false,
        scrollY: "calc(100vh - 300px)", //75vh
        scrollCollapse: true,
        info: false,
        dom: 'Brtip', //Bfrtip
        language: { "zeroRecords": "找不到資料" },
        "columnDefs": [
            { "visible": false, "targets": [ 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 18, 19, 20, 22 ] }
          ],
        buttons: [
          {
            extend:'colvis',
            text:'欄位選項'
          },
          {
            extend: 'colvisGroup',
            text: '預設顯示模式',
            show: [ 0, 1, 2, 3, 11, 15, 16, 17, 21 ],
            hide: [ 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 18, 19, 20, 22 ]
          },
        //   {
        //     extend: 'colvisGroup',
        //     text: '個人資料',
        //     show: [ 0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ],
        //     hide: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
        //  },
        //  {
        //    extend: 'colvisGroup',
        //    text: 'PI詳細資料',
        //    show: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
        //    hide: [ 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ]
        //  },
        //  {
        //     extend: 'colvisGroup',
        //     text: '顯示全部',
        //     show: ':hidden'
        //   },
          {
             extend: 'colvisGroup',
             text: '只顯示信箱',
             show: [ 15 ],
             hide: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22 ]
          }
        ]
    } );
    // table.button( 'showMails' ).trigger();
} );


////////// STAFF
$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#staff_table thead tr').clone(true).appendTo( '#staff_table thead' );
    $('#staff_table thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="搜尋 '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    var table = $('#staff_table').DataTable( {
        orderCellsTop: true,
        fixedHeader: true,
        paging: false,
        scrollY: "calc(100vh - 300px)", //75vh
        scrollCollapse: true,
        info: false,
        dom: 'Brtip', //Bfrtip
        language: { "zeroRecords": "找不到資料" },
        "columnDefs": [
            { "visible": false, "targets": [ 4, 5, 6, 7, 10, 11, 12, 16, 17, 18, 20 ] }
          ],
        buttons: [
          {
            extend:'colvis',
            text:'欄位選項'
          },
          {
            extend: 'colvisGroup',
            text: '預設顯示模式',
            show: [ 0, 1, 2, 3, 8, 9, 13, 14, 15, 19 ],
            hide: [ 4, 5, 6, 7, 10, 11, 12, 16, 17, 18, 20 ]
          },

          // {
          //   extend: 'colvisGroup',
          //   text: '個人資料',
          //   show: [ 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ],
          //   hide: [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
          // },
          // {
          //  extend: 'colvisGroup',
          //  text: '助理詳細資料',
          //  show: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
          //  hide: [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
          // },
          // {
          //   extend: 'colvisGroup',
          //   text: '顯示全部',
          //   show: ':hidden'
          // },
          {
             extend: 'colvisGroup',
             text: '只顯示信箱',
             show: [ 13 ],
             hide: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20 ]
          }
        ]
    } );
} );



$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#card_table thead tr').clone(true).appendTo( '#card_table thead' );
    $('#card_table thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="搜尋 '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    var table = $('#card_table').DataTable( {
        orderCellsTop: true,
        fixedHeader: true,
        paging: false,
        scrollY: "calc(100vh - 300px)", //75vh
        scrollCollapse: true,
        info: false,
        dom: 'Brtip', //Bfrtip
        language: { "zeroRecords": "找不到資料" },
        "columnDefs": [
            { "visible": false, "targets": [ 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ] }
          ],
        buttons: [
            {
              extend:'colvis',
              text:'欄位選項'
            },
            {
              extend: 'colvisGroup',
              text: '個人資料',
              show: [ 0, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ],
              hide: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            },
            {
              extend: 'colvisGroup',
              text: '門禁卡詳細資料',
              show: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
              hide: [ 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ]
            },
            {
              extend: 'colvisGroup',
              text: '預設顯示模式',
              show: [ 0, 1, 2, 7, 8, 9, 10, 11, 12 ],
              hide: [ 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ]
            },
            {
              extend: 'colvisGroup',
              text: '顯示全部',
              show: ':hidden'
            },
            {
               extend: 'colvisGroup',
               text: '只顯示信箱',
               show: [ 16 ],
               hide: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22 ]
            }

        ]
    } );
} );


/////////////////////////


// $(document).ready(function() {
//     // Setup - add a text input to each footer cell
//     $('#person_table thead tr').clone(true).appendTo( '#person_table thead' );
//     $('#person_table thead tr:eq(1) th').each( function (i) {
//         var title = $(this).text();
//         $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
//
//         $( 'input', this ).on( 'keyup change', function () {
//             if ( table.column(i).search() !== this.value ) {
//                 table
//                     .column(i)
//                     .search( this.value )
//                     .draw();
//             }
//         } );
//     } );
//
//     var table = $('#person_table').DataTable( {
//         orderCellsTop: true,
//         fixedHeader: true
//     } );
// } );
