private void FindCircle(PointF a, PointF b, PointF c,
    out PointF center, out float radius)
{

    float x1 = (b.X + a.X) / 2;
    float y1 = (b.Y + a.Y) / 2;
    float dy1 = b.X - a.X;
    float dx1 = -(b.Y - a.Y);

    float x2 = (c.X + b.X) / 2;
    float y2 = (c.Y + b.Y) / 2;
    float dy2 = c.X - b.X;
    float dx2 = -(c.Y - b.Y);

    bool lines_intersect, segments_intersect;
    PointF intersection, close1, close2;
    FindIntersection(
        new PointF(x1, y1), new PointF(x1 + dx1, y1 + dy1),
        new PointF(x2, y2), new PointF(x2 + dx2, y2 + dy2),
        out lines_intersect, out segments_intersect,
        out intersection, out close1, out close2);
    if (!lines_intersect)
    {
        MessageBox.Show("Точки коллинеарны");
        center = new PointF(0, 0);
        radius = 0;
    }
    else
    {
        center = intersection;
        float dx = center.X - a.X;
        float dy = center.Y - a.Y;
        radius = (float)Math.Sqrt(dx * dx + dy * dy);
    }
}