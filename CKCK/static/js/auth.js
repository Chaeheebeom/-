<script>
    function login() {
        var username = $('#username').val();
        var password = $('#password').val();

        if(username == '' || password == ''){
            alert('아이디 혹은 비밀번호를 입력해주세요');
        }else{
            $.ajax({
                url : "{{ url_for('auth.signin') }}",
                type : 'POST',
                data : { username:username, password:password },
                dataType : 'JSON',
                contentType: 'application/json;charset=UTF-8',
                success: function(res){
                    var Obj = JSON.parse(res);
                    console.log(Obj[0]);
                }
            });
        }
    }
</script>