function deleteCookie() {
  $.cookie('visiting', true, {
		expires: -1,
		path: '/'
	});
}

function setHandlers() {
	var ValidPassword = false;
	var ValidEmail = false;
	$('#id_email').bind("input", function()  
	{
		var email = document.getElementById('id_email');
		var btn = document.getElementById('id_submit');
		var p = document.getElementById('email_error');

		if (/^[\w\d]+([\.-]?[\w\d]+)*@[\w\d]+([\.-]?[\w\d]+)*(\.\w{2,3})+$/.test(email.value))  
		{
			$('#' + p.id).remove();
			email.className = "";
			ValidEmail = true;
			if(ValidPassword) { btn.disabled = false; }
		}
		else
		{
			if (!p)
			{
				var p = document.createElement('p');
				p.id = 'email_error';
				p.innerHTML = 'Данный адрес не корректен. Введите валидный.';
				p.className = 'error_message';
				$('#' + email.id).after(p);
			}

			email.className = 'errorfield';
			btn.disabled = true;
			ValidEmail = false;
		}
	});

	$('#id_username').bind("input", function()  
	{
		var email = document.getElementById('id_username');
		var btn = document.getElementById('id_submit');
		var p = document.getElementById('email_error');

		if (/^[\w\d]+([\.-]?[\w\d]+)*@[\w\d]+([\.-]?[\w\d]+)*(\.\w{2,3})+$/.test(email.value))  
		{
			$('#' + p.id).remove();
			email.className = "";
			ValidEmail = true;
			if(ValidPassword) { btn.disabled = false; }
		}
		else
		{
			if (!p)
			{
				var p = document.createElement('p');
				p.id = 'email_error';
				p.innerHTML = 'Данный адрес не корректен. Введите валидный.';
				p.className = 'error_message';
				$('#' + email.id).after(p);
			}

			email.className = 'errorfield';
			btn.disabled = true;
			ValidEmail = false;
		}
	});

	$('#id_password').bind("input", function()
	{
		var password = document.getElementById('id_password');
		var btn = document.getElementById('id_submit');
		var p = document.getElementById('password_error');

		if (password.value.length >= 5)  
		{
			$('#' + p.id).remove();
			password.className = "";
			ValidPassword = true;
			if (ValidEmail) { btn.disabled = false; }
		}
		else
		{
			if (!p)
			{
				var p = document.createElement('p');
				p.id = 'password_error';
				p.innerHTML = 'Пароль должен содержать не менее 5 символов.';
				p.className = 'error_message';
				$('#' + password.id).after(p);
			}

			password.className = 'errorfield';
			btn.disabled = true;
			ValidPassword = false;
		}
	});
}