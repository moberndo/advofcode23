using System.Text;

namespace aoc2024.Days;

internal class Day02 : Day
{
    protected override void Task1(IList<string> input, StringBuilder sb)
    {
        int safeCnt = 0;
        foreach (var line in input)
        {
            var values = line.Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(int.Parse);
            int agg = values.Last();
            for (int i = 0; i < values.Count() - 1; i++)
            {
                if (values.First() < values.Last())
                {
                    if (BadLevelDetectedAsc(values.ElementAt(i), values.ElementAt(i + 1)))
                        break;
                }
                else
                {
                    if (BadLevelDetectedDesc(values.ElementAt(i), values.ElementAt(i + 1)))
                        break;
                }
                agg += values.ElementAt(i);
            }
            var sum = values.Sum();
            if (agg == sum)
                safeCnt++;
        }

        sb.AppendLine(safeCnt.ToString());
    }

    protected override void Task2(IList<string> input, StringBuilder sb)
    {
        int safeCnt = 0;
        foreach (var line in input)
        {
            int badLevelCnt = 0;
            var values = line.Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(int.Parse);
            if (TryRecurse(values.ToList(), badLevelCnt))
                safeCnt++;
        }

        sb.AppendLine(safeCnt.ToString());
    }

    private static bool TryRecurse(IList<int> values, int badLevelCnt)
    {
        int agg = values.Last();
        for (int i = 0; i < values.Count - 1; i++)
        {
            if (values.First() < values.Last())
            {
                if (BadLevelDetectedAsc(values.ElementAt(i), values.ElementAt(i + 1)))
                {
                    if (badLevelCnt >= 1)
                        return false;
                    badLevelCnt++;
                    return TryRecurse(values.Where((v, idx) => idx != i).ToList(), badLevelCnt)
                        || TryRecurse(values.Where((v, idx) => idx != i + 1).ToList(), badLevelCnt);
                }
            }
            else
            {
                if (BadLevelDetectedDesc(values.ElementAt(i), values.ElementAt(i + 1)))
                {
                    if (badLevelCnt >= 1)
                        return false;
                    badLevelCnt++;
                    return TryRecurse(values.Where((v, idx) => idx != i).ToList(), badLevelCnt)
                        || TryRecurse(values.Where((v, idx) => idx != i + 1).ToList(), badLevelCnt);
                }
            }
            agg += values.ElementAt(i);
        }
        var sum = values.Sum();
        if (agg == sum)
            return true;
        return false;
    }

    private static bool BadLevelDetectedAsc(int element1, int element2)
    {
        var diff = Math.Abs(element1 - element2);
        return diff < 1 || diff > 3 || element1 > element2;
    }
    private static bool BadLevelDetectedDesc(int element1, int element2)
    {
        var diff = Math.Abs(element1 - element2);
        return diff < 1 || diff > 3 || element1 < element2;
    }
}
