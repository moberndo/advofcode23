using System.Text;

namespace aoc2024.Days;

internal class Day01 : Day
{
    protected override void Task1(IList<string> input, StringBuilder sb)
    {
        var col1 = ParseColumn(input, 0).OrderBy(x => x);
        var col2 = ParseColumn(input, 1).OrderBy(x => x);

        int sum = 0;
        for (int i = 0; i < col1.Count(); i++)
        {
            sum += Math.Abs(col1.ElementAt(i) - col2.ElementAt(i));
        }

        sb.AppendLine(sum.ToString());
    }

    protected override void Task2(IList<string> input, StringBuilder sb)
    {
        var col1 = ParseColumn(input, 0);
        var col2 = ParseColumn(input, 1);

        int sum = 0;
        foreach (var c1 in col1)
        {
            var cnt = col2.Count(c2 => c1 == c2);
            sum += c1 * cnt;
        }

        sb.AppendLine(sum.ToString());
    }

    private static IEnumerable<int> ParseColumn(IList<string> input, int index)
    {
        return input.Select(l =>
        {
            var elements = l.Split(' ', StringSplitOptions.RemoveEmptyEntries).ElementAt(index);
            return int.Parse(elements);
        });
    }
}
