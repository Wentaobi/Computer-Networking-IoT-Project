$("#btnAdd").click(function () {
    var name = $("#c_name").val();
    var desc = $("#c_desc").val();
    $.ajax({
        url: '/category.html',
        type: 'POST',
        dataType: 'json',
        data: {
            name: name,
            desc: desc,
        }
    });
    alert("请等待管理员审核！");
    window.location.href = "/";
});

$(".btnAdd").click(function () {
    var title = $("#title").val();
    var url = $("#url").val();
    var desc = $("#desc").val();
    var tag = $("#tag").val();
    var type = $("#type").val();
    if (title.trim()=="") {
        alert("标题不能为空！");
        return false;
    }
    if (url.trim()=="") {
        alert("地址不能为空！");
        return false;
    }
    if (desc.trim()=="") {
        alert("说明介绍不能为空！");
        return false;
    }
    if (type.trim()=="0") {
        alert("请选择文章分类！");
        return false;
    }
    $.ajax({
        url: '/sublimt.html',
        type: 'POST',
        dataType: 'json',
        data: {
            title: title,
            url: url,
            desc: desc,
            tag: tag,
            type: type
        }
    });
    alert("请等待管理员审核！");
    window.location.href = "/";
});

$("#btn_search").click(function () {
    var text = $("#search_text").val();
    if (text.trim() != "") {
        window.open("/index.html/" + text);
    }
});

function addInfoCategory() {
    $("#addInfoCate").modal();
}

function test() {
    alert("正在研发中...");
}

