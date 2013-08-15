;(function ( $, window, document, undefined ) {
    $.fn.extend({
        secureInput: function(options){
           var defaults = {
                fonts: ['Serif', 'Sans', 'Arial', 'Arial Black', 'Courier',
                    'Courier New', 'Comic Sans MS', 'Helvetica', 'Impact',
                    'Lucida Grande', 'Lucida Sans', 'Tahoma', 'Times',
                    'Times New Roman', 'Verdana'
                ]
            }

            var options = $.extend(defaults, options);

            var initToolbarBootstrapBindings = function(){
                var fonts = options.fonts,
                    fontTarget = $('[title=Font]').siblings('.dropdown-menu');
                $.each(fonts, function (idx, fontName) {
                    fontTarget.append($('<li><a data-edit="fontName ' + fontName +'" style="font-family:\''+ fontName +'\'">'+fontName + '</a></li>'));
                });
            }

            // creates html for font names
            initToolbarBootstrapBindings();

            return this.each(function(){
                var editors = $(this).find('.bootstrap-wysiwyg');
                editors.each(function(){
                    $(this).wysiwyg();
                });
                $(this).on('submit', function(){
                    $(this).find('.secure-input').each(function(){
                        var editor_id = $(this).attr("data-editor")
                        var editor_content = $("#"+editor_id).cleanHtml();
                        $(this).html(editor_content)
                    });
                });
                window.prettyPrint && prettyPrint();
            })
        }
    })
})( jQuery, window , document );