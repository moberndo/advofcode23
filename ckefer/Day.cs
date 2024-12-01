using System.Text;

namespace aoc2024;

internal abstract class Day : IDay
{
    private const string Root = @".\..\..\..\..";

    public void Run()
    {
        string className = GetType().Name;
        Console.WriteLine($"========== {className} ==========");
        var input = GetContent(className);

        StringBuilder sb = new();
        Task1(input, sb);
        Console.WriteLine("Task 1:");
        Console.WriteLine(sb.ToString());

        sb = new();
        Task2(input, sb);
        Console.WriteLine("Task 2:");
        Console.WriteLine(sb.ToString());
    }

    protected abstract void Task1(IList<string> input, StringBuilder sb);

    protected abstract void Task2(IList<string> input, StringBuilder sb);

    private static string[] GetContent(string className)
    {
        var folderPath = Path.Combine(Path.GetFullPath(Root), @"ckefer\Inputs");

        string filepath = @$"{folderPath}\{className}.txt";
        if (File.Exists(filepath))
            return File.ReadAllLines(filepath);

        throw new FileNotFoundException($"Path = '{filepath}'");
    }
}