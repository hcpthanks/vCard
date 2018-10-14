tinymce.init({
  selector    : 'textarea',
  height      : 500,
  theme       : 'modern',
  plugins     : 'print preview fullpage powerpaste searchreplace autolink directionality advcode visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists textcolor wordcount tinymcespellchecker a11ychecker imagetools mediaembed  linkchecker contextmenu colorpicker textpattern help',
  toolbar1    : 'formatselect | bold italic strikethrough forecolor backcolor | link | alignleft aligncenter alignright alignjustify  | numlist bullist outdent indent  | removeformat',
  image_advtab: true,
  templates   : [
    { title: 'Test template 1', content: 'Test 1' },
    { title: 'Test template 2', content: 'Test 2' }
  ],
  content_css: [
    // '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'
  ]
 });


// tinymce.init({
//   selector: 'textarea',
//   height  : 500,
//   menubar : false,
//   plugins : [
//     'advlist autolink lists link image charmap print preview anchor textcolor',
//     'searchreplace visualblocks code fullscreen',
//     'insertdatetime media table contextmenu paste code help wordcount'
//   ],
//   toolbar    : 'insert | undo redo |  formatselect | bold italic backcolor  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
//   content_css: [
//     // '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
//     '//www.tinymce.com/css/codepen.min.css']
// });





