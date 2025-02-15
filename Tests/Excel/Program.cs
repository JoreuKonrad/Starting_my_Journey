using OfficeOpenXml;
using OfficeOpenXml.Table;
using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        // Caminho para salvar o arquivo Excel
        var fileInfo = new FileInfo("PivotTableExample.xlsx");

        // Criar um novo pacote Excel
        using (var package = new ExcelPackage(fileInfo))
        {
            // Criar uma nova planilha
            var worksheet = package.Workbook.Worksheets.Add("Dados");
            var worksheet2 = package.Workbook.Worksheets.Add("tabela");

            // Preencher alguns dados de exemplo
            worksheet.Cells[1, 1].Value = "Produto";
            worksheet.Cells[1, 2].Value = "Categoria";
            worksheet.Cells[1, 3].Value = "Preço";
            worksheet.Cells[1, 4].Value = "Quantidade";

            worksheet.Cells[2, 1].Value = "Produto A";
            worksheet.Cells[2, 2].Value = "Categoria 1";
            worksheet.Cells[2, 3].Value = 10;
            worksheet.Cells[2, 4].Value = 100;

            worksheet.Cells[3, 1].Value = "Produto B";
            worksheet.Cells[3, 2].Value = "Categoria 1";
            worksheet.Cells[3, 3].Value = 20;
            worksheet.Cells[3, 4].Value = 150;

            worksheet.Cells[4, 1].Value = "Produto C";
            worksheet.Cells[4, 2].Value = "Categoria 2";
            worksheet.Cells[4, 3].Value = 30;
            worksheet.Cells[4, 4].Value = 200;

            worksheet.Cells[5, 1].Value = "Produto D";
            worksheet.Cells[5, 2].Value = "Categoria 2";
            worksheet.Cells[5, 3].Value = 40;
            worksheet.Cells[5, 4].Value = 250;

            // Criar uma Tabela Dinâmica
            var pivotTable = worksheet2.PivotTables.Add(worksheet2.Cells[1, 7], worksheet.Cells[1, 1, 5, 4], "PivotTable1");

            // Adicionar campos à Tabela Dinâmica
            pivotTable.RowFields.Add(pivotTable.Fields["Categoria"]);
            pivotTable.ColumnFields.Add(pivotTable.Fields["Produto"]);
            pivotTable.DataFields.Add(pivotTable.Fields["Preço"]);
            pivotTable.DataFields.Add(pivotTable.Fields["Quantidade"]);

            // Salvar o arquivo Excel
            package.Save();
        }

        Console.WriteLine("Tabela dinâmica criada com sucesso!");
    }
}
