$("#searchDbForm").submit(function (event) {
    event.preventDefault();
    var form = $(this);
    var query = $("#search_query").val();
    var searchType = $("input[name='search_type']:checked").val();
    $.ajax({
        type: "POST",
        url: "/search-database",
        dataType: 'json',
        data: { query: query, search_type: searchType },
        success: function (response) {
            $("#search_results").html("");
            if (searchType === "Books") {
                // Create table and header row
                var table = $("<table>").addClass("table table-compact");
                var headerRow = $("<tr>");
                headerRow.append($("<th>").text("ID"));
                headerRow.append($("<th>").text("Name"));
                headerRow.append($("<th>").text("Stock"));
                headerRow.append($("<th>").text("Actions"));
                table.append(headerRow);

                // Add a row for each book
                response.forEach(function (book) {
                    var row = $("<tr>");
                    row.append($("<td>").text(book.b_id));
                    row.append($("<td>").text(book.b_name));
                    row.append($("<td>").text(book.b_c_stock));
                    row.append($("<td>").append($("<a>").attr("href", "/edit-book/" + book.b_id).text("View")));
                    table.append(row);
                });

                // Append the table to the search results
                $("#search_results").html(table);
            } else if (searchType === "Members") {
                // Create table and header row
                var table = $("<table>").addClass("table table-compact");
                var headerRow = $("<tr>");
                headerRow.append($("<th>").text("ID"));
                headerRow.append($("<th>").text("Name"));
                headerRow.append($("<th>").text("Due Fees"));
                headerRow.append($("<th>").text("Books Issued"));
                headerRow.append($("<th>").text("Actions"));
                table.append(headerRow);

                // Add a row for each book
                response.forEach(function (member) {
                    var row = $("<tr>");
                    row.append($("<td>").text(member.m_id));
                    row.append($("<td>").text(member.m_name));
                    row.append($("<td>").text(member.m_due_fees));
                    row.append($("<td>").text(member.m_num_b_issued));
                    row.append($("<td>").append($("<a>").attr("href", "/edit-member/" + member.m_id).text("View")));
                    table.append(row);
                });

                // Append the table to the search results
                $("#search_results").html(table);
            } else if (searchType === "IssueRecords") {
                // Create table and header row
                var table = $("<table>").addClass("table table-compact");
                var headerRow = $("<tr>");
                headerRow.append($("<th>").text("ID"));
                headerRow.append($("<th>").text("Book ID"));
                headerRow.append($("<th>").text("Book Name"));
                headerRow.append($("<th>").text("Member ID"));
                headerRow.append($("<th>").text("Member Name"));
                headerRow.append($("<th>").text("Issue Date"));
                headerRow.append($("<th>").text("Return Date"));
                headerRow.append($("<th>").text("Actions"));
                table.append(headerRow);

                // Add a row for each book
                response.forEach(function (record) {
                    var row = $("<tr>");
                    row.append($("<td>").text(record.r_id));
                    row.append($("<td>").text(record.b_id));
                    row.append($("<td>").text(record.b_name));
                    row.append($("<td>").text(record.m_id));
                    row.append($("<td>").text(record.m_name));
                    row.append($("<td>").text(record.r_i_date));
                    row.append($("<td>").text(record.r_r_date));
                    row.append($("<td>").append($("<a>").attr("href", "/return-book/" + record.r_id).text("Return")));
                    table.append(row);
                });

                // Append the table to the search results
                $("#search_results").html(table);
            }
        }
    });
});