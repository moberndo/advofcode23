using System.Text;
using System.Text.RegularExpressions;

namespace aoc2024.Days;

internal class Day03 : Day
{
    protected override void Task1(IList<string> input, StringBuilder sb)
    {
        string singleLine = string.Join(null, input);
        int sum = 0;
        AddSumOfLine(singleLine, ref sum);

        sb.AppendLine(sum.ToString());
    }

    protected override void Task2(IList<string> input, StringBuilder sb)
    {
        string singleLine = string.Join(null, input);
        int sum = 0;
        var donts = singleLine.Split("don't()");
        for (int i = 0; i < donts.Length; i++)
        {
            var dont = donts[i];
            if (i == 0)
            {
                AddSumOfLine(dont, ref sum);
            }
            else
            {
                var dos = dont.Split("do()");
                foreach (var @do in dos.Skip(1))
                    AddSumOfLine(@do, ref sum);
            }
        }

        sb.AppendLine(sum.ToString());
    }

    private static void AddSumOfLine(string line, ref int sum)
    {
        var matches = Regex.Matches(line, @"mul\(([0-9]+,[0-9]+)\)");
        var values = matches.Cast<Match>().ToList().Select(m =>
        {
            if (m.Success)
            {
                var operands = m.Groups[1].Value.Split(',');
                return int.Parse(operands[0]) * int.Parse(operands[1]);
            }
            return 0;
        });
        sum += values.Sum();
    }
}
